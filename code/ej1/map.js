function() {
	key = this.productId;
	value = { 
		count: 1, //ocurrences
		score: parseInt(this.score,10)	//score as number 
	};
	emit(key, value);
}
