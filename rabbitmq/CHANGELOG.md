# CHANGELOG - rabbitmq

## 2.2.0 / 2021-09-30 / Agent 7.32.0

* [Added] Minor refactor. See [#10270](https://github.com/DataDog/integrations-core/pull/10270).
* [Added] Add HTTP option to control the size of streaming responses. See [#10183](https://github.com/DataDog/integrations-core/pull/10183).
* [Added] Add allow_redirect option. See [#10160](https://github.com/DataDog/integrations-core/pull/10160).
* [Fixed] Bump base package dependency. See [#10218](https://github.com/DataDog/integrations-core/pull/10218).
* [Fixed] Fix the description of the `allow_redirects` HTTP option. See [#10195](https://github.com/DataDog/integrations-core/pull/10195).

## 2.1.0 / 2021-09-17

* [Added] Disable generic tags. See [#10027](https://github.com/DataDog/integrations-core/pull/10027).

## 2.0.0 / 2021-08-22 / Agent 7.31.0

* [Fixed] Fix documented default value of `use_legacy_auth_encoding`. See [#9880](https://github.com/DataDog/integrations-core/pull/9880).
* [Changed] Remove messages for integrations for OK service checks. See [#9888](https://github.com/DataDog/integrations-core/pull/9888).

## 1.18.0 / 2021-06-23 / Agent 7.30.0

* [Added] Add runtime configuration validation. See [#8976](https://github.com/DataDog/integrations-core/pull/8976).

## 1.17.1 / 2021-03-07 / Agent 7.27.0

* [Fixed] Bump minimum base package version. See [#8443](https://github.com/DataDog/integrations-core/pull/8443).

## 1.17.0 / 2020-10-31 / Agent 7.24.0

* [Added] Add support for named groups in regular expressions. See [#7814](https://github.com/DataDog/integrations-core/pull/7814). Thanks [lkobus](https://github.com/lkobus).
* [Added] Add ability to dynamically get authentication information. See [#7660](https://github.com/DataDog/integrations-core/pull/7660).
* [Added] [doc] Add encoding in log config sample. See [#7708](https://github.com/DataDog/integrations-core/pull/7708).

## 1.16.0 / 2020-09-21 / Agent 7.23.0

* [Added] Add config specs. See [#7467](https://github.com/DataDog/integrations-core/pull/7467).
* [Fixed] Ensure basic auth encoding defaults to UTF-8. See [#7451](https://github.com/DataDog/integrations-core/pull/7451).
* [Fixed] Fix style for the latest release of Black. See [#7438](https://github.com/DataDog/integrations-core/pull/7438).

## 1.15.1 / 2020-08-10 / Agent 7.22.0

* [Fixed] Update ntlm_domain example. See [#7118](https://github.com/DataDog/integrations-core/pull/7118).

## 1.15.0 / 2020-06-29 / Agent 7.21.0

* [Added] Add note about warning concurrency. See [#6967](https://github.com/DataDog/integrations-core/pull/6967).
* [Added] Add head_message_timestamp metric. See [#6809](https://github.com/DataDog/integrations-core/pull/6809).
* [Fixed] Continue check execution when only a few vhosts are unhealthy. See [#6954](https://github.com/DataDog/integrations-core/pull/6954).

## 1.14.0 / 2020-05-17 / Agent 7.20.0

* [Added] Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).

## 1.13.1 / 2020-04-04 / Agent 7.19.0

* [Fixed] Update deprecated imports. See [#6088](https://github.com/DataDog/integrations-core/pull/6088).
* [Fixed] Remove logs sourcecategory. See [#6121](https://github.com/DataDog/integrations-core/pull/6121).

## 1.13.0 / 2020-02-22 / Agent 7.18.0

* [Added] Add option to disable node metrics in rabbitmq. See [#5750](https://github.com/DataDog/integrations-core/pull/5750).

## 1.12.0 / 2020-01-13 / Agent 7.17.0

* [Added] Use lazy logging format. See [#5398](https://github.com/DataDog/integrations-core/pull/5398).
* [Added] Use lazy logging format. See [#5377](https://github.com/DataDog/integrations-core/pull/5377).

## 1.11.0 / 2019-12-02 / Agent 7.16.0

* [Added] Add version metadata to RabbitMQ check. See [#4918](https://github.com/DataDog/integrations-core/pull/4918).

## 1.10.1 / 2019-10-18 / Agent 6.15.0

* [Fixed] Fix for rabbit 3.1 queue_totals introduced in #4668. See [#4805](https://github.com/DataDog/integrations-core/pull/4805).

## 1.10.0 / 2019-10-11

* [Added] verifies if `root` is dict before doing `.get`. See [#4668](https://github.com/DataDog/integrations-core/pull/4668).
* [Added] Add option to override KRB5CCNAME env var. See [#4578](https://github.com/DataDog/integrations-core/pull/4578).

## 1.9.2 / 2019-09-18

* [Fixed] Ignore empty data for metrics limit. See [#4544](https://github.com/DataDog/integrations-core/pull/4544).

## 1.9.1 / 2019-08-29 / Agent 6.14.0

* [Fixed] Revert "Fix queue, node and echange limit". See [#4467](https://github.com/DataDog/integrations-core/pull/4467).

## 1.9.0 / 2019-08-24

* [Added] Add mem_limit to RabbitMQ Checks. See [#4250](https://github.com/DataDog/integrations-core/pull/4250). Thanks [ParthKolekar](https://github.com/ParthKolekar).
* [Added] Add requests wrapper to RabbitMQ. See [#4257](https://github.com/DataDog/integrations-core/pull/4257).
* [Fixed] Fix queue, node and echange limit. See [#4108](https://github.com/DataDog/integrations-core/pull/4108).

## 1.8.0 / 2019-05-14 / Agent 6.12.0

* [Fixed] Fix default log path. See [#3611](https://github.com/DataDog/integrations-core/pull/3611).
* [Added] Adhere to code style. See [#3561](https://github.com/DataDog/integrations-core/pull/3561).

## 1.7.0 / 2019-01-04 / Agent 6.9.0

* [Added] Support Python 3. See [#2791][1].
* [Fixed] adds ignore_ssl_warning to rabbit file. See [#2706][2].

## 1.6.0 / 2018-11-30 / Agent 6.8.0

* [Added] Option to ignore SSL warnings. See [#2472][3]. Thanks [tebriel][4].
* [Fixed] Use raw string literals when \ is present. See [#2465][5].
* [Added] Add cluster wide metrics. See [#2449][6].

## 1.5.2 / 2018-09-04 / Agent 6.5.0

* [Fixed] Add data files to the wheel package. See [#1727][7].

## 1.5.1 / 2018-03-23

* [BUGFIX] URL encode queue names that might have special characters like '#'. See [#1100][8], thanks [@sylr][9].

## 1.5.0 / 2018-02-13

* [IMPROVEMENT] begin deprecation of `no_proxy` config flag in favor of `skip_proxy`. See [#1057][10].

## 1.4.0 / 2018-01-10

* [FEATURE] Add data collection for exchanges. See [#176][11]. (Thanks [@wholroyd][12])
* [FEATURE] Add a metric illustrating the available disk space. See [#902][13]. (Thanks [@dnavre][14])
* [BUGFIX] Assume a protocol if there isn't one, fixing a bug if you don't use a protocol. See [#909][15].
* [IMPROVEMENT] If vhosts are listed in the config, the check will only query for those specific vhosts, rather than querying for all of them. See [#910][16].
* [FEATURE] Add metrics to monitor a cluster. See [#924][17]

## 1.3.1 / 2017-10-10

* [BUGFIX] Add a key check before updating connection state metric. See [#729][18]. (Thanks [@ian28223][19])

## 1.3.0 / 2017-08-28

* [FEATURE] Add a metric to get the number of bindings for a queue. See [#674][20]
* [BUGFIX] Set aliveness service to CRITICAL if the rabbitmq server is down. See[#635][21]

## 1.2.0 / 2017-07-18

* [FEATURE] Add a metric about the number of connections to rabbitmq. See [#504][22]
* [FEATURE] Add custom tags to metrics, event and service checks. See [#506][23]
* [FEATURE] Add a metric about the number of each connection states. See [#514][24] (Thanks [@jamescarr][25])

## 1.1.0 / 2017-06-05

* [IMPROVEMENT] Disable proxy if so-desired. See [#407][26]

## 1.0.0 / 2017-03-22

* [FEATURE] adds rabbitmq integration.

[1]: https://github.com/DataDog/integrations-core/pull/2791
[2]: https://github.com/DataDog/integrations-core/pull/2706
[3]: https://github.com/DataDog/integrations-core/pull/2472
[4]: https://github.com/tebriel
[5]: https://github.com/DataDog/integrations-core/pull/2465
[6]: https://github.com/DataDog/integrations-core/pull/2449
[7]: https://github.com/DataDog/integrations-core/pull/1727
[8]: https://github.com/DataDog/integrations-core/issues/1100
[9]: https://github.com/sylr
[10]: https://github.com/DataDog/integrations-core/pull/1057
[11]: https://github.com/DataDog/integrations-core/pull/176
[12]: https://github.com/wholroyd
[13]: https://github.com/DataDog/integrations-core/issues/902
[14]: https://github.com/dnavre
[15]: https://github.com/DataDog/integrations-core/issues/909
[16]: https://github.com/DataDog/integrations-core/issues/910
[17]: https://github.com/DataDog/integrations-core/issues/924
[18]: https://github.com/DataDog/integrations-core/issues/729
[19]: https://github.com/ian28223
[20]: https://github.com/DataDog/integrations-core/issues/674
[21]: https://github.com/DataDog/integrations-core/issues/635
[22]: https://github.com/DataDog/integrations-core/issues/504
[23]: https://github.com/DataDog/integrations-core/issues/506
[24]: https://github.com/DataDog/integrations-core/issues/514
[25]: https://github.com/jamescarr
[26]: https://github.com/DataDog/integrations-core/issues/407
