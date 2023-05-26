const filters = document.querySelector('#filters');
const product_list = document.querySelector('#product-list');


const main = () => {
  fetch('http://127.0.0.1:8000/products/')
    .then(res => res.json())
    .then(data => {
      //call function
      createComponent(data)
    })
    .catch((error) => {
      console.log('Error:', error);
    })
}


const createComponent = (data) => {
  const products = document.createElement('div');
  products.classList.add('products')
  products.style.cssText = 'display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px;'

  data.forEach(product => {
    const productElem = document.createElement('div');
    productElem.className = 'product';
  
    productElem.innerHTML = `
      <div class="img-wrapper">
        <img src="${product.photo_url}" width="100%" alt="product image">
      </div>
      <p>${product.name}</p>
      <p>BDT-${product.price}</p>
      <div>
        <button class='primary'>Buy Now</button>
        <button class='secondary'>ADD TO CART</button>
      </div>
    `;

    products.appendChild(productElem);
  })

  product_list.appendChild(products)
}






main()



