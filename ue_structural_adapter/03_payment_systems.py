# Implement an adapter that allows an e-commerce application to interface with multiple types of payment systems
# (e.g., credit cards, PayPal, cryptocurrency wallets) using a unified method call.

# E-commerce platforms frequently need to process payments through different gateways (e.g., credit cards, PayPal,
# cryptocurrencies). Each system might have its own API and data requirements. Using an adapter for each payment type
# allows the application to interact with disparate payment services via a unified interface, reducing complexity and
# improving code maintainability.









if __name__ == '__main__':
    payment_processor = PaymentProcessor()
    paypal_adapter = PayPalAdapter(payment_processor)
    bitcoin_adapter = BitcoinAdapter(payment_processor)

    # Process payments using different systems through a unified interface
    paypal_adapter.process_payment(100.0, "USD")
    bitcoin_adapter.process_payment(0.0025, "BTC")



