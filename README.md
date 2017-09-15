# system_recomendation
...
# Arquivos
Dataset ./ml-100k
Script ./system_recomendation.py

# Link da referência
  https://www.analyticsvidhya.com/blog/2016/06/quick-guide-build-recommendation-engine-python/

# Saída do Programa
(943, 5)
(100000, 4)
(1682, 24)
This non-commercial license of GraphLab Create for academic use is assigned to brunoavli@hotmail.com and will expire on September 15, 2018.
[INFO] graphlab.cython.cy_server: GraphLab Create v2.1 started. Logging: /tmp/graphlab_server_1505439922.log
Recsys training: model = popularity
Warning: Ignoring columns unix_timestamp;
    To use these columns in scoring predictions, use a model that allows the use of additional features.
Preparing data set.
    Data has 90570 observations with 943 users and 1680 items.
    Data prepared in: 0.104139s
90570 observations to process; with 1680 unique items.
+---------+----------+-------+------+
| user_id | movie_id | score | rank |
+---------+----------+-------+------+
|    1    |   1467   |  5.0  |  1   |
|    1    |   1201   |  5.0  |  2   |
|    1    |   1189   |  5.0  |  3   |
|    1    |   1122   |  5.0  |  4   |
|    1    |   814    |  5.0  |  5   |
|    2    |   1467   |  5.0  |  1   |
|    2    |   1201   |  5.0  |  2   |
|    2    |   1189   |  5.0  |  3   |
|    2    |   1122   |  5.0  |  4   |
|    2    |   814    |  5.0  |  5   |
|    3    |   1467   |  5.0  |  1   |
|    3    |   1201   |  5.0  |  2   |
|    3    |   1189   |  5.0  |  3   |
|    3    |   1122   |  5.0  |  4   |
|    3    |   814    |  5.0  |  5   |
|    4    |   1467   |  5.0  |  1   |
|    4    |   1201   |  5.0  |  2   |
|    4    |   1189   |  5.0  |  3   |
|    4    |   1122   |  5.0  |  4   |
|    4    |   814    |  5.0  |  5   |
|    5    |   1467   |  5.0  |  1   |
|    5    |   1201   |  5.0  |  2   |
|    5    |   1189   |  5.0  |  3   |
|    5    |   1122   |  5.0  |  4   |
|    5    |   814    |  5.0  |  5   |
+---------+----------+-------+------+
[25 rows x 4 columns]

Recsys training: model = item_similarity
Warning: Ignoring columns unix_timestamp;
    To use these columns in scoring predictions, use a model that allows the use of additional features.
Preparing data set.
    Data has 90570 observations with 943 users and 1680 items.
    Data prepared in: 0.101736s
Training model from provided data.
Gathering per-item and per-user statistics.
+--------------------------------+------------+
| Elapsed Time (Item Statistics) | % Complete |
+--------------------------------+------------+
| 5.186ms                        | 100        |
+--------------------------------+------------+
Setting up lookup tables.
Processing data in one pass using dense lookup tables.
+-------------------------------------+------------------+-----------------+
| Elapsed Time (Constructing Lookups) | Total % Complete | Items Processed |
+-------------------------------------+------------------+-----------------+
| 12.061ms                            | 0.25             | 6               |
| 265.236ms                           | 100              | 1680            |
+-------------------------------------+------------------+-----------------+
Finalizing lookup tables.
Generating candidate set for working with new users.
Finished training in 1.27881s
+---------+----------+-------+------+
| user_id | movie_id | score | rank |
+---------+----------+-------+------+
|    1    |   1599   |  5.0  |  1   |
|    1    |   1201   |  5.0  |  2   |
|    1    |   1189   |  5.0  |  3   |
|    1    |   1122   |  5.0  |  4   |
|    1    |   814    |  5.0  |  5   |
|    2    |   1599   |  5.0  |  1   |
|    2    |   1201   |  5.0  |  2   |
|    2    |   1189   |  5.0  |  3   |
|    2    |   1122   |  5.0  |  4   |
|    2    |   814    |  5.0  |  5   |
|    3    |   1599   |  5.0  |  1   |
|    3    |   1201   |  5.0  |  2   |
|    3    |   1189   |  5.0  |  3   |
|    3    |   1122   |  5.0  |  4   |
|    3    |   814    |  5.0  |  5   |
|    4    |   1599   |  5.0  |  1   |
|    4    |   1201   |  5.0  |  2   |
|    4    |   1189   |  5.0  |  3   |
|    4    |   1122   |  5.0  |  4   |
|    4    |   814    |  5.0  |  5   |
|    5    |   1599   |  5.0  |  1   |
|    5    |   1201   |  5.0  |  2   |
|    5    |   1189   |  5.0  |  3   |
|    5    |   1122   |  5.0  |  4   |
|    5    |   814    |  5.0  |  5   |
+---------+----------+-------+------+
[25 rows x 4 columns]

PROGRESS: Evaluate model M0

Precision and recall summary statistics by cutoff
+--------+-------------------+-------------------+
| cutoff |   mean_precision  |    mean_recall    |
+--------+-------------------+-------------------+
|   1    |        0.0        |        0.0        |
|   2    |        0.0        |        0.0        |
|   3    |        0.0        |        0.0        |
|   4    |        0.0        |        0.0        |
|   5    |        0.0        |        0.0        |
|   6    | 0.000176740897844 | 0.000106044538706 |
|   7    | 0.000151492198152 | 0.000106044538706 |
|   8    | 0.000265111346766 | 0.000212089077413 |
|   9    | 0.000235654530458 | 0.000212089077413 |
|   10   | 0.000212089077413 | 0.000212089077413 |
+--------+-------------------+-------------------+
[10 rows x 3 columns]

PROGRESS: Evaluate model M1

Precision and recall summary statistics by cutoff
+--------+-------------------+-------------------+
| cutoff |   mean_precision  |    mean_recall    |
+--------+-------------------+-------------------+
|   1    |  0.00106044538706 | 0.000106044538706 |
|   2    | 0.000530222693531 | 0.000106044538706 |
|   3    | 0.000353481795688 | 0.000106044538706 |
|   4    | 0.000265111346766 | 0.000106044538706 |
|   5    | 0.000212089077413 | 0.000106044538706 |
|   6    | 0.000176740897844 | 0.000106044538706 |
|   7    | 0.000302984396304 | 0.000212089077413 |
|   8    | 0.000265111346766 | 0.000212089077413 |
|   9    | 0.000235654530458 | 0.000212089077413 |
|   10   | 0.000212089077413 | 0.000212089077413 |
+--------+-------------------+-------------------+
[10 rows x 3 columns]

Model compare metric: precision_recall
Canvas is accessible via web browser at the URL: http://localhost:51810/index.html
Opening Canvas in default web browser.
