# pyinstrument
Pyinstrument example
При запуске теста, запустится профайлер и напечатает в консоль результат выполнения, в котором покажет сколько расходуется ресурсов и времени.

Пример вывода:

```
1.802 Handle._run  asyncio\events.py:78
└─ 1.799 test_get_excel_file_link  sendout\sendout_core\tests\test_sendout_stats.py:20
   ├─ 1.779 SendoutStatsView.form_sendout_detail_stats_excel  sendout\sendout_core\sendout_stats.py:79
   │  ├─ 1.159 WriteSendoutFile.write_sendout_excel_file  sendout\sendout_core\sendout_file.py:188
   │  │  ├─ 0.629 SaveS3.upload_file_from_bytes  utilities\save_file.py:34
   │  │  │  └─ 0.629 S3._api_call  botocore\client.py:521
   │  │  │        [40 frames hidden]  botocore, urllib3, <built-in>, ssl, h...
   │  │  │           0.377 SSLContext.load_verify_locations  <built-in>
   │  │  ├─ 0.341 SaveS3.__init__  utilities\save_file.py:17
   │  │  │  ├─ 0.316 Session.client  boto3\session.py:217
   │  │  │  │     [36 frames hidden]  boto3, botocore, genericpath, <built-...
   │  │  │  └─ 0.025 Session.__init__  boto3\session.py:49
   │  │  │        [6 frames hidden]  boto3, botocore
   │  │  └─ 0.184 adjust_column_widths  sendout\sendout_core\sendout_file.py:211
   │  │     ├─ 0.107 XlsxWriter.__init__  pandas\io\excel\_xlsxwriter.py:185
   │  │     │     [5 frames hidden]  pandas, xlsxwriter, <built-in>
   │  │     └─ 0.070 XlsxWriter.__exit__  pandas\io\excel\_base.py:1364
   │  │           [13 frames hidden]  pandas, xlsxwriter, tempfile, <built-...
   │  └─ 0.615 SendoutStatsView._get_sendout_stats_df  sendout\sendout_core\sendout_stats.py:94
   │     ├─ 0.478 SendoutStatsView._get_batch_df  sendout\sendout_core\sendout_stats.py:129
   │     │  └─ 0.469 SendoutManagerDB.find_one_sendout_from_sendout_id  sendout\sendout_core\db_manager.py:86
   │     │     └─ 0.468 FindReqDB.find_one  database\api.py:454
   │     │        └─ 0.467 [await]  database\api.py
   │     ├─ 0.112 SendoutStatsView._get_data_for_records  sendout\sendout_core\sendout_stats.py:139
   │     │  └─ 0.103 SendoutRecordManagerDB.get_data_for_record_id_list  sendout\sendout_core\db_manager.py:221
   │     │     └─ 0.103 <listcomp>  sendout\sendout_core\db_manager.py:232
   │     │        └─ 0.103 AsyncIOMotorLatentCommandCursor.next  motor\core.py:1265
   │     │              [2 frames hidden]  motor
   │     └─ 0.025 _merge  sendout\sendout_core\sendout_stats.py:160
   └─ 0.018 get_conn  database\core.py:12
      └─ 0.018 AsyncIOMotorClient.__init__  motor\core.py:126
            [2 frames hidden]  motor, pymongo
```
