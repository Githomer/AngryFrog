function Remote($scope, SpeechService, Focus) {

	function showRemote() {
		const interfaces = require('os').networkInterfaces()
		let addresses = []
		for (let k in interfaces) {
			for (let k2 in interfaces[k]) {
				let address = interfaces[k][k2]
				if (address.family === 'IPv4' && !address.internal) {
					addresses.push(address.address)
				}
			}
		}
		$scope.remoteText = addresses[0] + ":" + config.remote.port;
		$scope.remoteImage = "https://chart.googleapis.com/chart?cht=qr&chs=400x400&chl=http://" + $scope.remoteText;
		Focus.change("remote");
	}
	
	
	
	
	/*$scope.remoteText = "allText";
	$scope.remoteImage = "/home/pi/show.jpg";
	Focus.change("remote");*/
/*	function FileReader(){
		//var reader = new FileReader();
		//reader.readAsText(file, "UTF-8");
	   	
		$scope.remoteText = "reader.result";
		$scope.remoteImage = "/home/pi/show.jpg";
		Focus.change("remote");
	}*/

	if (config.remote && config.remote.enabled) {
		SpeechService.addCommand('show_remoteQR', function () {
			//setInterval(FileReader(), 3000);
			showRemote()
		});
	} 
    

	$scope.remoteImage = "/home/pi/show.jpg";
	var check = 0;
    // First Run
	if (config.remote.firstRun) {
		$scope.firstRun = true;
		setInterval(function(){
			//Focus.change("remote");
			if (check == 0) {
				//alert("0");
				//$('#taeguk').hide();
				$scope.remoteImage = "/home/pi/show.jpg";
				check = 1;
			}
			else {
				//alert("1");
				//$('#taeguk').show(0);
				$scope.remoteImage = "/home/pi/show2.jpg";
				check = 0;
			}
			$('#taeguk').hide().show(0);
		}, 1000);
		Focus.change("remote");
		//showRemote()
	}
}

angular.module('SmartMirror')
    .controller('Remote', Remote);
