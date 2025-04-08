var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var itemId = this.dataset.item
		var action = this.dataset.action
		console.log('productId:', itemId, 'Action:', action)
        
        console.log('USER:', user)
        if (user == 'AnonymousUser'){
	        console.log('User is not authenticated')
			
        }else{
            updateUserOrder(itemId, action)
        }

	})
}

function updateUserOrder(itemID, action){
    var url = '/update-item/'
    console.log('URL:', url)
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'itemID': itemID, 'action':action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        location.reload()
    });
}