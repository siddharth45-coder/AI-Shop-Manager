const products = [
    {
        name: "Rice",
        price: 60,
        stock: 50
    },
    {
        name: "Sugar",
        price: 45,
        stock: 8
    },
    {
        name: "Cooking Oil",
        price: 150,
        stock: 20
    },
    {
        name: "Milk",
        price: 30,
        stock: 5
    },
    {
        name: "Biscuits",
        price: 20,
        stock: 40
    }
];

function loadProducts() {
    const productTable = document.getElementById("product-table");

    productTable.innerHTML = "";

    products.forEach(function(product) {
        const row = document.createElement("tr");

        let status;
        let statusClass;

        if (product.stock <= 10) {
            status = "Low Stock";
            statusClass = "low-stock";
        } else {
            status = "In Stock";
            statusClass = "in-stock";
        }

        row.innerHTML =
            "<td>" + product.name + "</td>" +
            "<td>₹" + product.price + "</td>" +
            "<td>" + product.stock + "</td>" +
            "<td class='" + statusClass + "'>" +
            status +
            "</td>";

        productTable.appendChild(row);
    });
}

function updateDashboard() {
    const totalProducts = products.length;

    const lowStockProducts = products.filter(function(product) {
        return product.stock <= 10;
    }).length;

    const todaySales = 1250;

    document.getElementById("total-products").textContent = totalProducts;

    document.getElementById("low-stock").textContent = lowStockProducts;

    document.getElementById("today-sales").textContent = "₹" + todaySales;
}

document.addEventListener("DOMContentLoaded", function() {
    loadProducts();
    updateDashboard();
});
