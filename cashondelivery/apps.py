from oscar.apps.checkout.app import CheckoutApplication

from . import views


class OverriddenCheckoutApplication(CheckoutApplication):
    # Specify new view for payment details
    payment_details_view = get_class('checkout', 'PaymentDetailsView')
