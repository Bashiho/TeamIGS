function changeQuantity(itemId, action){
    console.log('USER:', user)
    // Commented out some lines to prevent errors when signed into admin account
    // Add back if/when accounts are implemented
    // if (user == 'AnonymousUser'){
    // console.log('User not authenticated')
    addCookieItem(itemId, action)
    // }else{
        // console.log('User authenticated')
        // updateUserOrder(itemId, action)
    // }
}

function updateUserOrder(itemId, action){
    var url = '/updateItem/'
    console.log('URL:', url)
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'itemId': itemId, 'action':action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        location.reload()
    });
}

function addCookieItem(itemId, action){
    console.log('User not authenticated')
    if (action == 'add'){
        if(cart[itemId] == undefined){
            cart[itemId] = {'quantity':1}
        }
        else{
            cart[itemId]['quantity'] += 1
        }
    }
    else if (action == 'remove'){
        cart[itemId]['quantity'] -= 1

        if(cart[itemId]['quantity'] <= 0){
            delete cart[itemId];
        }
    }
    console.log("Cart:", cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}