async function rpc_execute(model, method, args) {
	return new Promise((resolve,reject) =>{
		const XHR = new XMLHttpRequest();
		XHR.open("POST",'/rpc');
		XHR.setRequestHeader('Content-Type', 'application/json');
		const data = {
			model: model,
			function: method,
			arguments: args
		}
		XHR.send(JSON.stringify(data));
		XHR.onreadystatechange=function(){
			console.log(XHR.response);
			resolve(return_val);
		}
	})
}