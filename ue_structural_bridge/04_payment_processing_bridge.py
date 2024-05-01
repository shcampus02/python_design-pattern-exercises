# Scenario: E-commerce systems and mobile apps often need to integrate with multiple payment gateways to accommodate
# various payment methods preferred by users, like Stripe for credit cards, PayPal for e-wallets, or Square for
# point-of-sale transactions.
#
# Explanation: The Bridge pattern isolates the payment processing logic from the specifics of each payment gateway.
# This allows the main payment handling code to remain constant even as new payment gateways are added or modified,
# providing a more adaptable and maintainable payment infrastructure.

# Design a bridge pattern that abstracts the complexity of handling different payment gateways (e.g., Stripe, PayPal,
# Square).






if __name__ == '__main__':
    stripe_payment_processor = StripePaymentProcessor()
    paypal_payment_processor = PayPalPaymentProcessor()

    payment_manager = PaymentManager(stripe_payment_processor)
    payment_manager.process_payment(100.0)

    payment_manager.switch_processor(paypal_payment_processor)
    payment_manager.process_payment(200.0)
