var updateBtns = document.getElementsByClassName('update-cart')


for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var postId = this.dataset.post
        var action = this.dataset.action
        var itemValue = this.dataset.value
        console.log('postId:', postId, 'action:', action, 'itemValue:', itemValue)

        console.log('USER:', user)
        if(user === 'AnonymousUser'){
            addCookieItem(postId, action)
        }else{
            updateUserOrder(postId, action, itemValue)
         }
    })

}

function addCookieItem(postId, action){
    console.log('not logged in.. ')

    if (action == 'add'){
        if(cart[postId] == undefined){
            cart[postId] = {'quantity':1}
        }else{
            cart[postId]['quantity'] += 1
        }
    }

    if (action == 'remove'){
        cart[postId]['quantity'] -= 1

        if(cart[postId]['quantity]'] <= 0){
            console.log('remove item')
            delete cart[postId]
        }
    }
    console.log('cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()

}

function updateUserOrder(postId, action, itemValue){
    console.log('User is logged inm sending data ..')

    var url = '/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'postId': postId, 'action': action, 'itemValue': itemValue,})
    }) 

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}
