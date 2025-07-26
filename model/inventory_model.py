#######################
# Sample Project Data #
#######################

data_materials_json = {
    'material_id': {
        '1': {
            'name': 'caster wheels',
            'type': 'misc',
            'qty_low': '10',
            'qty_stock': "100",
            'qty_planned': "5",
            'qty_reserved': "0",
        },
        '2': {
            'name': '2in PVC Elbow',
            'type': 'pvc',
            'qty_low': '10',
            'qty_stock': "100",
            'qty_planned': "5",
            'qty_reserved': "0",
        },
        '3': {
            'name': '2x4 Cedar',
            'type': 'wood',
            'qty_low': '10',
            'qty_stock': "95",
            'qty_planned': "15",
            'qty_reserved': "5",
        },
        '4': {
            'name': '3/8in Plywood Sheet',
            'type': 'wood',
            'qty_low': '10',
            'qty_stock': "60",
            'qty_planned': "40",
            'qty_reserved': "40",
        },
        '5': {
            'name': '2in Aluminum Rod',
            'type': 'aluminum',
            'qty_low': '10',
            'qty_stock': "80",
            'qty_planned': "20",
            'qty_reserved': "20",
        },
        '6': {
            'name': '1.5in 10-24 zinc screw',
            'type': 'screw',
            'qty_low': '10',
            'qty_stock': "99",
            'qty_planned': "1",
            'qty_reserved': "1",
        },
        '7': {
            'name': 'sheet rock 4x8ft',
            'type': 'sheetrock',
            'qty_low': '10',
            'qty_stock': "100",
            'qty_planned': "10",
            'qty_reserved': "0",
        },
        '8': {
            'name': 'white wood primer 1 gallon',
            'type': 'paint',
            'qty_low': '10',
            'qty_stock': "100",
            'qty_planned': "0",
            'qty_reserved': "0",
        },
        '9': {
            'name': 'epoxy resin 1 qt',
            'type': 'epoxy',
            'qty_low': '10',
            'qty_stock': "80",
            'qty_planned': "20",
            'qty_reserved': "20",
        },
    }
}

data_project_bom = [
                                ("1", "2", "5", "0"),
                                ("1", "3", "15", "5"),
                                ("1", "4", "20", "20"),
                                ("2", "1", "5", "5"),
                                ("2", "6", "1", "1"),
                                ("2", "7", "10", "0"),
                                ("3", "4", "20", "20"),
                                ("3", "5", "20", "20"),
                                ("3", "9", "20", "20"),
                            ]


def get_all_materials():
    return data_materials_json['material_id']


def get_material_details_by_id(uid):
    return data_materials_json['material_id'][uid]

def post_new_material(name, material_type, low_qty):
    next_material_id = str(len(get_all_materials().keys()))

    data_materials_json['material_id'][next_material_id] = {
        'name': name,
        'type': material_type,
        'qty_low': low_qty,
    }

    return data_materials_json['material_id'][next_material_id]


def get_material_where_used_by_id(uid):
    return {
            'project_id': {
                '1': {
                    'title': 'Bird Mansion',
                    'qty_planned': '10',
                    'qty_reserved': '5',
                },
                '2': {
                    'title': 'Wickham Park Renovation',
                    'qty_planned': '5',
                    'qty_reserved': '10',
                }
            }
        }



