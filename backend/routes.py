from flask import request, jsonify
from models import db, Income, Expense, Budget, Asset, Debt, Saving

def register_routes(app):
    @app.route('/api/incomes', methods=['GET', 'POST'])
    def incomes():
        if request.method == 'POST':
            data = request.json
            inc = Income(source=data['source'], amount=data['amount'])
            db.session.add(inc); db.session.commit()
            return jsonify({"id": inc.id}), 201
        else:
            items = Income.query.order_by(Income.date.desc()).all()
            return jsonify([{"id": i.id, "source": i.source, "amount": i.amount, "date": i.date.isoformat()} for i in items])

    @app.route('/api/expenses', methods=['GET', 'POST'])
    def expenses():
        if request.method == 'POST':
            data = request.json
            ex = Expense(category=data['category'], description=data.get('description'), amount=data['amount'])
            db.session.add(ex); db.session.commit()
            return jsonify({"id": ex.id}), 201
        else:
            items = Expense.query.order_by(Expense.date.desc()).all()
            return jsonify([{"id": e.id, "category": e.category, "description": e.description, "amount": e.amount, "date": e.date.isoformat()} for e in items])

    @app.route('/api/budgets', methods=['GET', 'POST'])
    def budgets():
        if request.method == 'POST':
            data = request.json
            b = Budget(category=data['category'], limit=data['limit'])
            db.session.add(b); db.session.commit()
            return jsonify({"id": b.id}), 201
        else:
            items = Budget.query.all()
            return jsonify([{"id": b.id, "category": b.category, "limit": b.limit} for b in items])

    @app.route('/api/assets', methods=['GET', 'POST'])
    def assets():
        if request.method == 'POST':
            data = request.json
            a = Asset(name=data['name'], value=data['value'])
            db.session.add(a); db.session.commit()
            return jsonify({"id": a.id}), 201
        else:
            items = Asset.query.all()
            return jsonify([{"id": a.id, "name": a.name, "value": a.value} for a in items])

    @app.route('/api/debts', methods=['GET', 'POST'])
    def debts():
        if request.method == 'POST':
            data = request.json
            d = Debt(name=data['name'], balance=data['balance'], interest_rate=data['interest_rate'], minimum_payment=data['minimum_payment'])
            db.session.add(d); db.session.commit()
            return jsonify({"id": d.id}), 201
        else:
            items = Debt.query.all()
            return jsonify([{"id": d.id, "name": d.name, "balance": d.balance, "interest_rate": d.interest_rate, "minimum_payment": d.minimum_payment} for d in items])

    @app.route('/api/savings', methods=['GET', 'POST'])
    def savings():
        if request.method == 'POST':
            data = request.json
            s = Saving(name=data['name'], goal=data['goal'], current=data.get('current', 0.0), strategy=data.get('strategy'))
            db.session.add(s); db.session.commit()
            return jsonify({"id": s.id}), 201
        else:
            items = Saving.query.all()
            return jsonify([{"id": s.id, "name": s.name, "goal": s.goal, "current": s.current, "strategy": s.strategy} for s in items])