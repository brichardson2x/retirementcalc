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

