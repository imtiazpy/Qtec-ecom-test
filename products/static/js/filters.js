window.addEventListener('DOMContentLoaded', () => {
  const filterProducts = () => {
    const selectedBrands = getSelectedCheckboxes('brand');
    const selectedCategories = getSelectedCheckboxes('category');
    const selectedTypes = getSelectedCheckboxes('type');
    const minPrice = document.querySelector('input[name="min_price"]').value;
    const maxPrice = document.querySelector('input[name="max_price"]').value;
    const selectedWarranty = getSelectedCheckboxes('warranty');
    const selectedSellers = getSelectedCheckboxes('seller');

    const url = buildFilterURL({
      selectedBrands,
      selectedCategories,
      selectedTypes,
      minPrice,
      maxPrice,
      selectedWarranty,
      selectedSellers
    });

    window.location.href = url;
  };

  const getSelectedCheckboxes = (name) => {
    const checkboxes = Array.from(document.querySelectorAll(`input[name="${name}"]:checked`));
    return checkboxes.map(checkbox => checkbox.value);
  };

  const buildFilterURL = ({
    selectedBrands,
    selectedCategories,
    selectedTypes,
    minPrice,
    maxPrice,
    selectedWarranty,
    selectedSellers
  }) => {
    const brandParam = selectedBrands.length ? `brand=${selectedBrands.join('&brand=')}` : '';
    const categoryParam = selectedCategories.length ? `category=${selectedCategories.join('&category=')}` : '';
    const typeParam = selectedTypes.length ? `type=${selectedTypes.join('&type=')}` : '';
    const minPriceParam = minPrice ? `min_price=${minPrice}` : '';
    const maxPriceParam = maxPrice ? `max_price=${maxPrice}` : '';
    const warrantyParam = selectedWarranty.length ? `warranty=${selectedWarranty.join('&warranty=')}` : '';
    const sellerParam = selectedSellers.length ? `seller=${selectedSellers.join('&seller=')}` : '';

    const queryParams = [brandParam, categoryParam, typeParam, minPriceParam, maxPriceParam, warrantyParam, sellerParam];
    const filteredParams = queryParams.filter(param => param !== '');
    const url = `/?${filteredParams.join('&')}`;

    return url;
  };

  const checkboxes = document.querySelectorAll('input[type="checkbox"]');
  checkboxes.forEach((checkbox) => checkbox.addEventListener('change', filterProducts));
});