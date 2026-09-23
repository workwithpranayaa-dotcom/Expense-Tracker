# Product notes

ShopForge is intentionally an operations-first commerce product rather than a simple storefront.

Important domain rules:
- inventory changes are transactional
- an order has an immutable set of order items and prices
- payment confirmation comes from a verified provider webhook
- returns create inventory events rather than silently changing stock
- admin actions should be auditable

Suggested production integrations: Stripe/Razorpay sandbox, object storage for product media, email receipts, background jobs, and Redis for cache/rate limiting.
