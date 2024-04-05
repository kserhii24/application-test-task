# 1. 
```
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 2983.0
python_gc_objects_collected_total{generation="1"} 381.0
python_gc_objects_collected_total{generation="2"} 22.0
# HELP python_gc_objects_uncollectable_total Uncollectable objects found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 123.0
python_gc_collections_total{generation="1"} 11.0
python_gc_collections_total{generation="2"} 1.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="11",patchlevel="9",version="3.11.9"} 1.0
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 13.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1.048576e+06
# HELP request_count Total request count
# TYPE request_count gauge
request_count{endpoint="/ready",hostname="behavox-deployment-575b7c9b5b-zj67f"} 42.0
request_count{endpoint="/health",hostname="behavox-deployment-575b7c9b5b-zj67f"} 21.0
request_count{endpoint="/payload",hostname="behavox-deployment-575b7c9b5b-zj67f"} 33.0
request_count{endpoint="/metrics",hostname="behavox-deployment-575b7c9b5b-zj67f"} 1.0
# HELP response_time Response time in milliseconds
# TYPE response_time gauge
response_time{endpoint="/ready",hostname="behavox-deployment-575b7c9b5b-zj67f"} 0.23049999992963421
response_time{endpoint="/health",hostname="behavox-deployment-575b7c9b5b-zj67f"} 0.8244160000003831
response_time{endpoint="/payload",hostname="behavox-deployment-575b7c9b5b-zj67f"} 0.18983299992214597
# HELP positive_response_count_total Count of positive response codes
# TYPE positive_response_count_total counter
positive_response_count_total{endpoint="/ready",hostname="behavox-deployment-575b7c9b5b-zj67f",status_code="200"} 42.0
positive_response_count_total{endpoint="/health",hostname="behavox-deployment-575b7c9b5b-zj67f",status_code="200"} 21.0
positive_response_count_total{endpoint="/payload",hostname="behavox-deployment-575b7c9b5b-zj67f",status_code="200"} 33.0
# HELP positive_response_count_created Count of positive response codes
# TYPE positive_response_count_created gauge
positive_response_count_created{endpoint="/ready",hostname="behavox-deployment-575b7c9b5b-zj67f",status_code="200"} 1.7123279139143167e+09
positive_response_count_created{endpoint="/health",hostname="behavox-deployment-575b7c9b5b-zj67f",status_code="200"} 1.7123279237694194e+09
positive_response_count_created{endpoint="/payload",hostname="behavox-deployment-575b7c9b5b-zj67f",status_code="200"} 1.7123281412182612e+09
```

# 2. 
```
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 2928.0
python_gc_objects_collected_total{generation="1"} 330.0
python_gc_objects_collected_total{generation="2"} 94.0
# HELP python_gc_objects_uncollectable_total Uncollectable objects found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 124.0
python_gc_collections_total{generation="1"} 11.0
python_gc_collections_total{generation="2"} 1.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="11",patchlevel="9",version="3.11.9"} 1.0
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 13.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1.048576e+06
# HELP request_count Total request count
# TYPE request_count gauge
request_count{endpoint="/health",hostname="behavox-deployment-575b7c9b5b-wtbqq"} 19.0
request_count{endpoint="/ready",hostname="behavox-deployment-575b7c9b5b-wtbqq"} 37.0
request_count{endpoint="/payload",hostname="behavox-deployment-575b7c9b5b-wtbqq"} 35.0
request_count{endpoint="/metrics",hostname="behavox-deployment-575b7c9b5b-wtbqq"} 1.0
# HELP response_time Response time in milliseconds
# TYPE response_time gauge
response_time{endpoint="/health",hostname="behavox-deployment-575b7c9b5b-wtbqq"} 0.14316699991923088
response_time{endpoint="/ready",hostname="behavox-deployment-575b7c9b5b-wtbqq"} 1.696082999956161
response_time{endpoint="/payload",hostname="behavox-deployment-575b7c9b5b-wtbqq"} 0.2387499999940701
# HELP positive_response_count_total Count of positive response codes
# TYPE positive_response_count_total counter
positive_response_count_total{endpoint="/health",hostname="behavox-deployment-575b7c9b5b-wtbqq",status_code="200"} 19.0
positive_response_count_total{endpoint="/ready",hostname="behavox-deployment-575b7c9b5b-wtbqq",status_code="200"} 37.0
positive_response_count_total{endpoint="/payload",hostname="behavox-deployment-575b7c9b5b-wtbqq",status_code="200"} 35.0
# HELP positive_response_count_created Count of positive response codes
# TYPE positive_response_count_created gauge
positive_response_count_created{endpoint="/health",hostname="behavox-deployment-575b7c9b5b-wtbqq",status_code="200"} 1.7123280257285802e+09
positive_response_count_created{endpoint="/ready",hostname="behavox-deployment-575b7c9b5b-wtbqq",status_code="200"} 1.71232802573151e+09
positive_response_count_created{endpoint="/payload",hostname="behavox-deployment-575b7c9b5b-wtbqq",status_code="200"} 1.7123281389073064e+09
```

# 3. 
```
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 3372.0
python_gc_objects_collected_total{generation="1"} 323.0
python_gc_objects_collected_total{generation="2"} 86.0
# HELP python_gc_objects_uncollectable_total Uncollectable objects found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 124.0
python_gc_collections_total{generation="1"} 11.0
python_gc_collections_total{generation="2"} 1.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="11",patchlevel="9",version="3.11.9"} 1.0
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 13.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1.048576e+06
# HELP request_count Total request count
# TYPE request_count gauge
request_count{endpoint="/ready",hostname="behavox-deployment-575b7c9b5b-c4gc6"} 45.0
request_count{endpoint="/health",hostname="behavox-deployment-575b7c9b5b-c4gc6"} 22.0
request_count{endpoint="/payload",hostname="behavox-deployment-575b7c9b5b-c4gc6"} 35.0
request_count{endpoint="/metrics",hostname="behavox-deployment-575b7c9b5b-c4gc6"} 1.0
# HELP response_time Response time in milliseconds
# TYPE response_time gauge
response_time{endpoint="/ready",hostname="behavox-deployment-575b7c9b5b-c4gc6"} 0.7767089999788368
response_time{endpoint="/health",hostname="behavox-deployment-575b7c9b5b-c4gc6"} 0.30579200006286555
response_time{endpoint="/payload",hostname="behavox-deployment-575b7c9b5b-c4gc6"} 0.19733300007374055
# HELP positive_response_count_total Count of positive response codes
# TYPE positive_response_count_total counter
positive_response_count_total{endpoint="/ready",hostname="behavox-deployment-575b7c9b5b-c4gc6",status_code="200"} 45.0
positive_response_count_total{endpoint="/health",hostname="behavox-deployment-575b7c9b5b-c4gc6",status_code="200"} 22.0
positive_response_count_total{endpoint="/payload",hostname="behavox-deployment-575b7c9b5b-c4gc6",status_code="200"} 35.0
# HELP positive_response_count_created Count of positive response codes
# TYPE positive_response_count_created gauge
positive_response_count_created{endpoint="/ready",hostname="behavox-deployment-575b7c9b5b-c4gc6",status_code="200"} 1.712327964725832e+09
positive_response_count_created{endpoint="/health",hostname="behavox-deployment-575b7c9b5b-c4gc6",status_code="200"} 1.7123279744377573e+09
positive_response_count_created{endpoint="/payload",hostname="behavox-deployment-575b7c9b5b-c4gc6",status_code="200"} 1.7123281402883682e+09
```
