import oss

s3 = oss.resource('s3', endpoint_url='https://gateway.99265.net',
                  access_key_id='jxe2ayxct2zrypz2ghrk7ws74ofq',
                  secret_access_key='j2mpch2wa3upgkgshcmdal5fyncdikdouwemk4tjrnsvjrsnduh5e',
                  )
bucketName = "buc1"
bucket = s3.Bucket(bucketName)
prefix = '/'
if not prefix:
    objects = bucket.objects.all()
else:
    objects = bucket.objects.filter(Prefix=prefix)
    for obj in objects:
        print(obj.key)
