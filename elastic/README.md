# Elasticsearch Integration

![Elasitc search dashboard][1]

## Overview

Stay up-to-date on the health of your Elasticsearch cluster, from its overall status down to JVM heap usage and everything in between. Get notified when you need to revive a replica, add capacity to the cluster, or otherwise tweak its configuration. After doing so, track how your cluster metrics respond.

The Datadog Agent's Elasticsearch check collects metrics for search and indexing performance, memory usage and garbage collection, node availability, shard statistics, disk space and performance, pending tasks, and many more. The Agent also sends events and service checks for the overall status of your cluster.

## Setup

### Installation

The Elasticsearch check is included in the [Datadog Agent][2] package. No additional installation is necessary.

### Configuration

<!-- xxx tabs xxx -->
<!-- xxx tab "Host" xxx -->

#### Host

To configure this check for an Agent running on a host:

##### Metric collection

1. Edit the `elastic.d/conf.yaml` file, in the `conf.d/` folder at the root of your [Agent's configuration directory][3] to start collecting your Elasticsearch [metrics](#metrics). See the [sample elastic.d/conf.yaml][4] for all available configuration options.

   ```yaml
   init_config:

   instances:
     ## @param url - string - required
     ## The URL where Elasticsearch accepts HTTP requests. This is used to
     ## fetch statistics from the nodes and information about the cluster health.
     #
     - url: http://localhost:9200
   ```

    **Notes**:

      - If you're collecting Elasticsearch metrics from just one Datadog Agent running outside the cluster, such as using a hosted Elasticsearch, set `cluster_stats` to `true`.
      - [Agent-level tags][5] are not applied to hosts in a cluster that is not running the Agent. Use integration level tags in `<integration>.d/conf.yaml` to ensure **ALL** metrics have consistent tags. For example:

        ```yaml
        init_config:
        instances:
          - url: "%%env_MONITOR_ES_HOST%%"
            username: "%%env_MONITOR_ES_USER%%"
            password: *********
            auth_type: basic
            cluster_stats: true
            tags:
            - service.name:elasticsearch
            - env:%%env_DD_ENV%%
        ```

      - To use the Agent's Elasticsearch integration for the AWS Elasticsearch services, set the `url` parameter to point to your AWS Elasticsearch stats URL.
      - All requests to the Amazon ES configuration API must be signed. See the [AWS documentation][6] for details.
      - The `aws` auth type relies on [boto3][7] to automatically gather AWS credentials from `.aws/credentials`. Use `auth_type: basic` in the `conf.yaml` and define the credentials with `username: <USERNAME>` and `password: <PASSWORD>`.

2. [Restart the Agent][8].

##### Trace collection

Datadog APM integrates with Elasticsearch to see the traces across your distributed system. Trace collection is enabled by default in the Datadog Agent v6+. To start collecting traces:

1. [Enable trace collection in Datadog][9].
2. [Instrument your application that makes requests to ElasticSearch][10].

##### Log collection

<!-- partial
{{< site-region region="us3" >}}
**Log collection is not supported for the Datadog {{< region-param key="dd_site_name" >}} site**.
{{< /site-region >}}
partial -->

_Available for Agent versions >6.0_

1. Collecting logs is disabled by default in the Datadog Agent, enable it in the `datadog.yaml` file with:

   ```yaml
   logs_enabled: true
   ```

2. To collect search slow logs and index slow logs, [configure your Elasticsearch settings][11]. By default, slow logs are not enabled.

   - To configure index slow logs for a given index `<INDEX>`:

     ```shell
     curl -X PUT "localhost:9200/<INDEX>/_settings?pretty" -H 'Content-Type: application/json' -d' {
       "index.indexing.slowlog.threshold.index.warn": "0ms",
       "index.indexing.slowlog.threshold.index.info": "0ms",
       "index.indexing.slowlog.threshold.index.debug": "0ms",
       "index.indexing.slowlog.threshold.index.trace": "0ms",
       "index.indexing.slowlog.level": "trace",
       "index.indexing.slowlog.source": "1000"
     }'
     ```

   - To configure search slow logs for a given index `<INDEX>`:

     ```shell
     curl -X PUT "localhost:9200/<INDEX>/_settings?pretty" -H 'Content-Type: application/json' -d' {
       "index.search.slowlog.threshold.query.warn": "0ms",
       "index.search.slowlog.threshold.query.info": "0ms",
       "index.search.slowlog.threshold.query.debug": "0ms",
       "index.search.slowlog.threshold.query.trace": "0ms",
       "index.search.slowlog.threshold.fetch.warn": "0ms",
       "index.search.slowlog.threshold.fetch.info": "0ms",
       "index.search.slowlog.threshold.fetch.debug": "0ms",
       "index.search.slowlog.threshold.fetch.trace": "0ms"
     }'
     ```

3. Add this configuration block to your `elastic.d/conf.yaml` file to start collecting your Elasticsearch logs:

   ```yaml
   logs:
     - type: file
       path: /var/log/elasticsearch/*.log
       source: elasticsearch
       service: "<SERVICE_NAME>"
   ```

   - Add additional instances to start collecting slow logs:

     ```yaml
     - type: file
       path: "/var/log/elasticsearch/\
             <CLUSTER_NAME>_index_indexing_slowlog.log"
       source: elasticsearch
       service: "<SERVICE_NAME>"

     - type: file
       path: "/var/log/elasticsearch/\
             <CLUSTER_NAME>_index_search_slowlog.log"
       source: elasticsearch
       service: "<SERVICE_NAME>"
     ```

     Change the `path` and `service` parameter values and configure them for your environment.

4. [Restart the Agent][8].

<!-- xxz tab xxx -->
<!-- xxx tab "Docker" xxx -->

#### Docker

To configure this check for an Agent running on a container:

##### Metric collection

Set [Autodiscovery Integrations Templates][12] as Docker labels on your application container:

```yaml
LABEL "com.datadoghq.ad.check_names"='["elastic"]'
LABEL "com.datadoghq.ad.init_configs"='[{}]'
LABEL "com.datadoghq.ad.instances"='[{"url": "http://%%host%%:9200"}]'
```

##### Log collection

<!-- partial
{{< site-region region="us3" >}}
**Log collection is not supported for the Datadog {{< region-param key="dd_site_name" >}} site**.
{{< /site-region >}}
partial -->


Collecting logs is disabled by default in the Datadog Agent. To enable it, see the [Docker log collection documentation][13].

Then, set [Log Integrations][14] as Docker labels:

```yaml
LABEL "com.datadoghq.ad.logs"='[{"source":"elasticsearch","service":"<SERVICE_NAME>"}]'
```

##### Trace collection

APM for containerized apps is supported on Agent v6+ but requires extra configuration to begin collecting traces.

Required environment variables on the Agent container:

| Parameter            | Value                                                                      |
| -------------------- | -------------------------------------------------------------------------- |
| `<DD_API_KEY>` | `api_key`                                                                  |
| `<DD_APM_ENABLED>`      | true                                                              |
| `<DD_APM_NON_LOCAL_TRAFFIC>`  | true |

See [Tracing Kubernetes Applications][15] and the [Kubernetes Daemon Setup][16] for a complete list of available environment variables and configuration.

Then, [instrument your application container][10] and set `DD_AGENT_HOST` to the name of your Agent container.


<!-- xxz tab xxx -->
<!-- xxx tab "Kubernetes" xxx -->

#### Kubernetes

To configure this check for an Agent running on Kubernetes:

##### Metric collection

Set [Autodiscovery Integrations Templates][17] as pod annotations on your application container. Aside from this, templates can also be configured with [a file, a configmap, or a key-value store][18].

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: elasticsearch
  annotations:
    ad.datadoghq.com/elasticsearch.check_names: '["elastic"]'
    ad.datadoghq.com/elasticsearch.init_configs: '[{}]'
    ad.datadoghq.com/elasticsearch.instances: |
      [
        {
          "url": "http://%%host%%:9200"
        }
      ]
spec:
  containers:
    - name: elasticsearch
```

##### Log collection

<!-- partial
{{< site-region region="us3" >}}
**Log collection is not supported for the Datadog {{< region-param key="dd_site_name" >}} site**.
{{< /site-region >}}
partial -->


Collecting logs is disabled by default in the Datadog Agent. To enable it, see the [Kubernetes log collection documentation][19].

Then, set [Log Integrations][14] as pod annotations. This can also be configured with [a file, a configmap, or a key-value store][20].

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: elasticsearch
  annotations:
    ad.datadoghq.com/elasticsearch.logs: '[{"source":"elasticsearch","service":"<SERVICE_NAME>"}]'
spec:
  containers:
    - name: elasticsearch
```

##### Trace collection

APM for containerized apps is supported on hosts running Agent v6+ but requires extra configuration to begin collecting traces.

Required environment variables on the Agent container:

| Parameter            | Value                                                                      |
| -------------------- | -------------------------------------------------------------------------- |
| `<DD_API_KEY>` | `api_key`                                                                  |
| `<DD_APM_ENABLED>`      | true                                                              |
| `<DD_APM_NON_LOCAL_TRAFFIC>`  | true |

See [Tracing Kubernetes Applications][15] and the [Kubernetes Daemon Setup][16] for a complete list of available environment variables and configuration.

Then, [instrument your application container][10] and set `DD_AGENT_HOST` to the name of your Agent container.

<!-- xxz tab xxx -->
<!-- xxx tab "ECS" xxx -->

#### ECS

To configure this check for an Agent running on ECS:

##### Metric collection

Set [Autodiscovery Integrations Templates][12] as Docker labels on your application container:

```json
{
  "containerDefinitions": [{
    "name": "elasticsearch",
    "image": "elasticsearch:latest",
    "dockerLabels": {
      "com.datadoghq.ad.check_names": "[\"elastic\"]",
      "com.datadoghq.ad.init_configs": "[{}]",
      "com.datadoghq.ad.instances": "[{\"url\": \"http://%%host%%:9200\"}]"
    }
  }]
}
```

##### Log collection

<!-- partial
{{< site-region region="us3" >}}
**Log collection is not supported for the Datadog {{< region-param key="dd_site_name" >}} site**.
{{< /site-region >}}
partial -->


Collecting logs is disabled by default in the Datadog Agent. To enable it, see the [ECS log collection documentation][21].

Then, set [Log Integrations][14] as Docker labels:

```json
{
  "containerDefinitions": [{
    "name": "elasticsearch",
    "image": "elasticsearch:latest",
    "dockerLabels": {
      "com.datadoghq.ad.logs": "[{\"source\":\"elasticsearch\",\"service\":\"<SERVICE_NAME>\"}]"
    }
  }]
}
```

##### Trace collection

APM for containerized apps is supported on Agent v6+ but requires extra configuration to begin collecting traces.

Required environment variables on the Agent container:

| Parameter            | Value                                                                      |
| -------------------- | -------------------------------------------------------------------------- |
| `<DD_API_KEY>` | `api_key`                                                                  |
| `<DD_APM_ENABLED>`      | true                                                              |
| `<DD_APM_NON_LOCAL_TRAFFIC>`  | true |

See [Tracing Kubernetes Applications][15] and the [Kubernetes Daemon Setup][16] for a complete list of available environment variables and configuration.

Then, [instrument your application container][10] and set `DD_AGENT_HOST` to the [EC2 private IP address][22].


<!-- xxz tab xxx -->
<!-- xxz tabs xxx -->

### Validation

[Run the Agent's status subcommand][23] and look for `elastic` under the Checks section.

## Data Collected

By default, not all of the following metrics are sent by the Agent. To send all metrics, configure flags in `elastic.yaml` as shown above.

- `pshard_stats` sends **elasticsearch.primaries.\*** and **elasticsearch.indices.count** metrics
- `index_stats` sends **elasticsearch.index.\*** metrics
- `pending_task_stats` sends **elasticsearch.pending\_\*** metrics

For version >=6.3.0, set `xpack.monitoring.collection.enabled` configuration to `true` in your Elasticsearch configuration in order to collect all `elasticsearch.thread_pool.write.*` metrics. See [Elasticsearch release notes - monitoring section][24].

### Metrics

See [metadata.csv][25] for a list of metrics provided by this integration.

### Events

The Elasticsearch check emits an event to Datadog each time the overall status of your Elasticsearch cluster changes - red, yellow, or green.

### Service Checks

See [service_checks.json][26] for a list of service checks provided by this integration.

## Troubleshooting

- [Agent can't connect][27]
- [Why isn't Elasticsearch sending all my metrics?][11]

## Further Reading

To get a better idea of how (or why) to integrate your Elasticsearch cluster with Datadog, check out our [series of blog posts][28] about it.

[1]: https://raw.githubusercontent.com/DataDog/integrations-core/master/elastic/images/elasticsearch-dash.png
[2]: https://app.datadoghq.com/account/settings#agent
[3]: https://docs.datadoghq.com/agent/guide/agent-configuration-files/#agent-configuration-directory
[4]: https://github.com/DataDog/integrations-core/blob/master/elastic/datadog_checks/elastic/data/conf.yaml.example
[5]: https://docs.datadoghq.com/getting_started/tagging/assigning_tags?tab=noncontainerizedenvironments#file-location
[6]: https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-ac.html#es-managedomains-signing-service-requests
[7]: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#configuring-credentials
[8]: https://docs.datadoghq.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[9]: https://docs.datadoghq.com/tracing/send_traces/
[10]: https://docs.datadoghq.com/tracing/setup/
[11]: https://docs.datadoghq.com/integrations/faq/why-isn-t-elasticsearch-sending-all-my-metrics/
[12]: https://docs.datadoghq.com/agent/docker/integrations/?tab=docker
[13]: https://docs.datadoghq.com/agent/docker/log/?tab=containerinstallation#installation
[14]: https://docs.datadoghq.com/agent/docker/log/?tab=containerinstallation#log-integrations
[15]: https://docs.datadoghq.com/agent/kubernetes/apm/?tab=java
[16]: https://docs.datadoghq.com/agent/kubernetes/daemonset_setup/?tab=k8sfile#apm-and-distributed-tracing
[17]: https://docs.datadoghq.com/agent/kubernetes/integrations/?tab=kubernetes
[18]: https://docs.datadoghq.com/agent/kubernetes/integrations/?tab=kubernetes#configuration
[19]: https://docs.datadoghq.com/agent/kubernetes/log/?tab=containerinstallation#setup
[20]: https://docs.datadoghq.com/agent/kubernetes/log/?tab=daemonset#configuration
[21]: https://docs.datadoghq.com/agent/amazon_ecs/logs/?tab=linux
[22]: https://docs.datadoghq.com/agent/amazon_ecs/apm/?tab=ec2metadataendpoint#setup
[23]: https://docs.datadoghq.com/agent/guide/agent-commands/#agent-status-and-information
[24]: https://www.elastic.co/guide/en/elasticsearch/reference/6.3/release-notes-6.3.0.html
[25]: https://github.com/DataDog/integrations-core/blob/master/elastic/metadata.csv
[26]: https://github.com/DataDog/integrations-core/blob/master/elastic/assets/service_checks.json
[27]: https://docs.datadoghq.com/integrations/faq/elastic-agent-can-t-connect/
[28]: https://www.datadoghq.com/blog/monitor-elasticsearch-performance-metrics
