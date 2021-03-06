/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 * 
 * http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
package org.apache.ambari.logsearch.domain;

import com.github.dockerjava.api.DockerClient;
import com.github.dockerjava.core.DockerClientConfig;
import org.apache.solr.client.solrj.impl.CloudSolrClient;

public class StoryDataRegistry {
  public static final StoryDataRegistry INSTANCE = new StoryDataRegistry();

  private DockerClient dockerClient;
  private DockerClientConfig dockerClientConfig;
  private CloudSolrClient cloudSolrClient;
  private boolean logsearchContainerStarted = false;
  private String dockerHost;
  private String ambariFolder;
  private final int solrPort = 8886;
  private final int logsearchPort = 61888;
  private final int zookeeperPort = 9983;
  private final String serviceLogsCollection = "hadoop_logs";
  private final String auditLogsCollection = "audit_logs";

  private StoryDataRegistry() {
  }

  public String getDockerHost() {
    return dockerHost;
  }

  public void setDockerHost(String dockerHost) {
    this.dockerHost = dockerHost;
  }

  public int getSolrPort() {
    return solrPort;
  }

  public int getLogsearchPort() {
    return logsearchPort;
  }

  public int getZookeeperPort() {
    return zookeeperPort;
  }

  public DockerClient getDockerClient() {
    return dockerClient;
  }

  public void setDockerClient(DockerClient dockerClient) {
    this.dockerClient = dockerClient;
  }

  public String getServiceLogsCollection() {
    return serviceLogsCollection;
  }

  public String getAuditLogsCollection() {
    return auditLogsCollection;
  }

  public CloudSolrClient getCloudSolrClient() {
    return cloudSolrClient;
  }

  public void setCloudSolrClient(CloudSolrClient cloudSolrClient) {
    this.cloudSolrClient = cloudSolrClient;
  }

  public String getAmbariFolder() {
    return ambariFolder;
  }

  public void setAmbariFolder(String ambariFolder) {
    this.ambariFolder = ambariFolder;
  }

  public DockerClientConfig getDockerClientConfig() {
    return dockerClientConfig;
  }

  public void setDockerClientConfig(DockerClientConfig dockerClientConfig) {
    this.dockerClientConfig = dockerClientConfig;
  }

  public boolean isLogsearchContainerStarted() {
    return logsearchContainerStarted;
  }

  public void setLogsearchContainerStarted(boolean logsearchContainerStarted) {
    this.logsearchContainerStarted = logsearchContainerStarted;
  }
}
