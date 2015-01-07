function (key, reducedValue) { 
	if(reducedValue.count >= 20){
		return reducedValue.score/reducedValue.count;	//average score
	}
	else{
		return 0;
	}
}
