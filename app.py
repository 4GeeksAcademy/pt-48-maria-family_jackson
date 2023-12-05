from flask import Flask, request, jsonify
from datastructures import Family

app = Flask(__name__)

jackson_family = Family('Jackson')

@app.route('/members', methods=['GET'])
def get_all_members():
    try:
        family_members = jackson_family.get_all_members()

        if not family_members:
            return jsonify({'error': 'No se encontraron miembros de la familia'}), 400
        return jsonify({'family_members': family_members}), 200

    except Exception as e:
        return jsonify({'error': 'Error interno del servidor'}), 500

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    try:
        member = jackson_family.get_member(member_id)

        if member is None:
            return jsonify({'error': 'Miembro no encontrado'}), 404

        return jsonify({'member': member}), 200

    except Exception as e:
        return jsonify({'error': 'Error interno del servidor'}), 500

@app.route('/members', methods=['POST'])
def add_member():
    try:
        new_member_data = request.json
        new_member = jackson_family.add_member(new_member_data)

        return jsonify({'member': new_member}), 200

    except Exception as e:
        return jsonify({'error': 'Error interno del servidor'}), 500

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):

    deleted = jackson_family.delete_member(member_id)

    if deleted:
        return jsonify({'message': 'Miembro eliminado correctamente'}), 200
    else:
        return jsonify({'error': 'Miembro no encontrado'}), 404

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    try:
        updated_member_data = request.json
        updated = jackson_family.update_member(member_id, updated_member_data)

        if updated:
            return jsonify({'message': 'Miembro actualizado correctamente'}), 200
        else:
            return jsonify({'error': 'Miembro no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': 'Error interno del servidor'}), 500

if __name__ == '__main__':
    app.run(debug=True)

