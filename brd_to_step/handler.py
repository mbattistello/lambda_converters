from __future__ import print_function

import json
import os


from aws_s3 import AwsS3
from conversion_error import ConversionError
from brd_to_step import build
from step_to_stl import convert

STL_KEY_PREFIX = 'cad_files/stl/'
STEP_KEY_PREFIX = 'cad_files/stp/'

def lambda_handler(event, context):
    print('Running lambda_handler...')

    #get data from request/event
    s3_bucket = event.get('s3_bucket')
    s3_object = event.get('s3_object')

    #check event params
    if not s3_bucket:
        raise ConversionError('No s3_bucket provided')

    if not s3_object:
        raise ConversionError('No s3_object provided')

    #create local path
    local_step = '/tmp/' + os.path.basename(s3_object)
    

    #init s3 object to help with s3 get/put
    s3 = AwsS3()

    print('Fetching {}/{} and saving to {}'.format(s3_bucket,
                                                   s3_object,
                                                   local_step))

    #get step from s3. put in local tmp
    s3.get_object(s3_bucket, s3_object, local_step)

    #create stl file name from step file name
    stl_file = os.path.splitext(local_step)[0] + '.stl'

    

    print('Converting {} to {}'.format(local_step, stl_file))

    #calls step to stl code to convert it
    convert(local_step, stl_file)  #source, dest

    #build step
    step_file = '/tmp/brd.step'
    build( step_file )

    #creates prefix/path to put stl file in s3
    s3_key = STL_KEY_PREFIX + os.path.basename(stl_file)

    s3_step_key = STEP_KEY_PREFIX + 'brd.step'

    print('Uploading {} to {}/{}'.format(stl_file, s3_bucket, s3_key))

    #puts file in s3 from local tmp
    s3.put_object(stl_file, s3_bucket, s3_key)

    print('Uploading {} to {}/{}'.format(step_file, s3_bucket, s3_step_key))

    s3.put_object(step_file, s3_bucket, s3_step_key)
