"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

import os

from ambari_commons.constants import AMBARI_SUDO_BINARY
from resource_management.libraries.script import Script
from resource_management.libraries.script.script import get_config_lock_file
from resource_management.libraries.functions import default
from resource_management.libraries.functions import conf_select
from resource_management.libraries.functions import stack_select
from resource_management.libraries.functions import format_jvm_option
from resource_management.libraries.functions.version import format_stack_version
from string import lower

config = Script.get_config()
tmp_dir = Script.get_tmp_dir()

dfs_type = default("/commandParams/dfs_type", "")

is_parallel_execution_enabled = int(default("/agentConfigParams/agent/parallel_execution", 0)) == 1
host_sys_prepped = default("/hostLevelParams/host_sys_prepped", False)

sudo = AMBARI_SUDO_BINARY

stack_version_unformatted = config['hostLevelParams']['stack_version']
stack_version_formatted = format_stack_version(stack_version_unformatted)

# current host stack version
current_version = default("/hostLevelParams/current_version", None)

# service name
service_name = config['serviceName']

# logsearch configuration
logsearch_logfeeder_conf = "/etc/ambari-logsearch-logfeeder/conf"

agent_cache_dir = config['hostLevelParams']['agentCacheDir']
service_package_folder = config['commandParams']['service_package_folder']
logsearch_service_name = service_name.lower().replace("_", "-")
logsearch_config_file_name = 'input.config-' + logsearch_service_name + ".json"
logsearch_config_file_path = agent_cache_dir + "/" + service_package_folder + "/templates/" + logsearch_config_file_name + ".j2"
logsearch_config_file_exists = os.path.exists(logsearch_config_file_path)

# default hadoop params
mapreduce_libs_path = "/usr/lib/hadoop-mapreduce/*"
hadoop_libexec_dir = stack_select.get_hadoop_dir("libexec")
hadoop_conf_empty_dir = "/etc/hadoop/conf.empty"

# HDP 2.2+ params
if Script.is_stack_greater_or_equal("2.2"):
  mapreduce_libs_path = "/usr/hdp/current/hadoop-mapreduce-client/*"

  # not supported in HDP 2.2+
  hadoop_conf_empty_dir = None

versioned_stack_root = '/usr/hdp/current'

#security params
security_enabled = config['configurations']['cluster-env']['security_enabled']

#java params
java_home = config['hostLevelParams']['java_home']

#hadoop params
hdfs_log_dir_prefix = config['configurations']['hadoop-env']['hdfs_log_dir_prefix']
hadoop_pid_dir_prefix = config['configurations']['hadoop-env']['hadoop_pid_dir_prefix']
hadoop_root_logger = config['configurations']['hadoop-env']['hadoop_root_logger']

jsvc_path = "/usr/lib/bigtop-utils"

hadoop_heapsize = config['configurations']['hadoop-env']['hadoop_heapsize']
namenode_heapsize = config['configurations']['hadoop-env']['namenode_heapsize']
namenode_opt_newsize = config['configurations']['hadoop-env']['namenode_opt_newsize']
namenode_opt_maxnewsize = config['configurations']['hadoop-env']['namenode_opt_maxnewsize']
namenode_opt_permsize = format_jvm_option("/configurations/hadoop-env/namenode_opt_permsize","128m")
namenode_opt_maxpermsize = format_jvm_option("/configurations/hadoop-env/namenode_opt_maxpermsize","256m")

jtnode_opt_newsize = "200m"
jtnode_opt_maxnewsize = "200m"
jtnode_heapsize =  "1024m"
ttnode_heapsize = "1024m"

dtnode_heapsize = config['configurations']['hadoop-env']['dtnode_heapsize']
mapred_pid_dir_prefix = default("/configurations/mapred-env/mapred_pid_dir_prefix","/var/run/hadoop-mapreduce")
mapred_log_dir_prefix = default("/configurations/mapred-env/mapred_log_dir_prefix","/var/log/hadoop-mapreduce")

#users and groups
hdfs_user = config['configurations']['hadoop-env']['hdfs_user']
user_group = config['configurations']['cluster-env']['user_group']

namenode_host = default("/clusterHostInfo/namenode_host", [])
has_namenode = not len(namenode_host) == 0

if has_namenode or dfs_type == 'HCFS':
  hadoop_conf_dir = conf_select.get_hadoop_conf_dir(force_latest_on_upgrade=True)

link_configs_lock_file = get_config_lock_file()
stack_select_lock_file = os.path.join(tmp_dir, "stack_select_lock_file")

upgrade_suspended = default("/roleParams/upgrade_suspended", False)
