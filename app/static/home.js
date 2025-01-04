document.addEventListener('DOMContentLoaded', function() {
    const formatCurrency = (input) => {
        let value = input.value.replace(/[^0-9.]/g, '');
        if (value) {
            value = parseFloat(value).toLocaleString('en-US', { style: 'currency', currency: 'USD' });
        }
        input.value = value;
    };

    const formatPercentage = (input) => {
        let value = input.value.replace(/[^0-9.]/g, '');
        if (value) {
            value = parseFloat(value).toFixed(2) + '%';
        }
        input.value = value;
    };

    const balanceInputs = document.querySelectorAll('input[name$="_balance"]');
    const contributionInputs = document.querySelectorAll('input[name^="monthly_contribution"]');
    const percentageInputs = document.querySelectorAll('input[name$="_rate"], input[name$="_return"]');

    balanceInputs.forEach(input => {
        input.addEventListener('blur', () => formatCurrency(input));
    });

    contributionInputs.forEach(input => {
        input.addEventListener('blur', () => formatCurrency(input));
    });

    percentageInputs.forEach(input => {
        input.addEventListener('blur', () => formatPercentage(input));
    });

    document.querySelectorAll('input').forEach(input => {
        input.addEventListener('input', () => {
            input.value = input.value.replace(/[^0-9.]/g, '');
        });
    });
});

document.getElementById('retire_form').addEventListener('submit', function(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    const jsondata = Object.fromEntries(formData.entries());

    const jsonstring = JSON.stringify(jsondata);

    console.log(jsonstring);

    fetch('http://localhost:80/calculator', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: jsonstring,
    })

    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
    })
    .then(result => {
        console.log('Success:', result);
    })
    .then(error => {
        console.error('Error:', error);
    });

})


/*



*/