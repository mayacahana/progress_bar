import sys

def upload_callback(current, total):
    status = 'Uploading... '
    bar_len = 60
    filled_len = int(round(bar_len*current / float(total)))
    percnt = round(100.0 * current / float(total), 1)
    bar = '='*filled_len+ '-'*(bar_len - filled_len)
    sys.stdout.write('[%s]%s%s ...%s\r'%(bar,percnt,'%',status))
    sys.stdout.flush()
