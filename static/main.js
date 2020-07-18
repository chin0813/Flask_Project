function rpc_execute(model, method, args) {
	//2020-07-18: Still unable to get return value directly when calling this function. Might need to use other libraries.
	const XHR = new XMLHttpRequest();
	return new Promise((resolve,reject) =>{
		XHR.open("POST",'/rpc');
		XHR.setRequestHeader('Content-Type', 'application/json');
		const data = {
			model: model,
			function: method,
			arguments: args
		}
		XHR.send(JSON.stringify(data));
		XHR.onreadystatechange=function(){
			resolve(XHR);
		}
	})
}