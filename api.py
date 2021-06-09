import random
import string
from flask import Flask, jsonify, request
from base import Session
from brand import Brand
from discountcode import DiscountCode, DiscountCodeState


app = Flask(__name__)

error_invalid_brand_id = { 'description': 'invalid brand id' }
success = { 'description': 'success' }


@app.route('/discountcode/brand/generate/<brandid>/<count>', methods=['POST'])
def generate_discount_code(brandid, count):
    session = Session()
    brands = session.query(Brand).filter(Brand.id == brandid).all()
    if len(brands) == 0:
        return jsonify(error_invalid_brand_id), 400

    # generate code and save to db
    for i in range(int(count)):
        letters = string.ascii_uppercase
        code = ''.join(random.choice(letters) for j in range(10))
        session.add(DiscountCode(brandid, code))

    session.commit()
    session.close()
    return jsonify(success)


@app.route('/discountcode/brand/fetch/<brandid>')
def get_discount_code(brandid):
    session = Session()
    brand = session.query(Brand).filter(Brand.id == brandid).all().pop(0)

    if brand is None:
        return jsonify(error_invalid_brand_id)

    discountcode = session.query(DiscountCode).filter(Brand.id == brandid).\
        filter(DiscountCode.state == DiscountCodeState.UNUSED).limit(1).all().pop(0)
    discountcode.state = DiscountCodeState.DISTRIBUTED
    session.commit()

    return jsonify({'brand': brand.brand_name, 'discountcode': discountcode.code})
