import braintree

from flask import Flask, render_template, request

app = Flask(__name__)

braintree.Configuration.configure(
    braintree.Environment.Sandbox,
merchant_id="v4wm7rs86jb85ycs",
public_key="8n9hvpbqn2b37tjy",
private_key="dbb4b7948310f37953901b7789d2d927"
)

@app.route('/')
def index():
	ClientToken = braintree.ClientToken.generate()
	print "abc"
	return render_template('detail.html', ClientToken=ClientToken)

@app.route("/checkout", methods=["POST"])
def create_purchase():
		nonce = request.form["payment_method_nonce"]
		print(nonce)
		result = braintree.Transaction.sale({
	    			"amount": "10.00",
	    			"payment_method_nonce": nonce
		})
		if result.is_success:
			return "<h1>Success! Transaction ID: {0} </h1>".format(result.transaction.id)
		else:
			return "<h1>Error: {0}</h1>".format(result.message)

if __name__ == '__main__':
	app.run()