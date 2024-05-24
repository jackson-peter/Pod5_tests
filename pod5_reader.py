import pod5

pod5_file="/ssd_workspace/jpeter/tests_Fast5Pod5/basecalled_pod5/PAU17537_5cc8219e_4e669770_777.pod5"
pod5_bc_dir="/ssd_workspace/jpeter/tests_Fast5Pod5/basecalled_pod5"

# Iterate over every record in the file using reads()
with pod5.Reader(pod5_file) as reader:
    for read_record in reader.reads():
        print(read_record.read_id)

# Iterate over every record in the dataset using __iter__
with pod5.DatasetReader(pod5_bc_dir, recursive=True) as dataset:
    for read_record in dataset:
        print(read_record.read_id, read_record.path)



