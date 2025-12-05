from pydantic import BaseModel


class RequestPurchaseItemIdSchema(BaseModel):
    purchase_item_id: int


class RequestGiftsSchema(BaseModel):
    purchase_item_id: int
    payment_id: int
    user_id: int


class RequestCreateStripeProductSchema(BaseModel):
    purchase_item_id: int
    payment_id: int
