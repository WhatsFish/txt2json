# txt2json
A little tool which used to convert txt file into json format
---
## from a txt file
```plain
张三;24;Peking University
李四;24;Northwestern Polytechnical University
张五;27;Xidian University
赵六;30;Wuhan University
孙伟;23;Tsinghua University
张超;24;Peking University
李明;24;Northwestern Polytechnical University
张迎;27;Xidian University
赵四;30;Wuhan University
王坤;23;Tsinghua University
孙伟;23;Tsinghua University
刘帅;25;Fudan University
```
## to a json
```json
{
    "school_info" : {
                     "total_count": 6,
                     "detail"     : {
                                      "Peking University": 2,
                                      "Northwestern Polytechnical University": 2,
                                      "Xidian University": 2,
                                      "Wuhan University": 2,
                                      "Tsinghua University": 3,
                                      "Fudan University": 1,
                                     },
    "asc_age_list" : [23, 23, 23, 24, 24, 24, 24, 25, 27, 27, 30, 30],
    "desc_age_list": [30, 30, 27, 27, 25, 24, 24, 24, 24, 23, 23, 30]
}
```
