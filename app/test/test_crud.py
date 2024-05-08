from app.src.crud import YourClassName


def test_item_init():
    item = Item(1, "item1", "description1")
    assert item.id == 1
    assert item.name == "item1"
    assert item.description == "description1"


def test_item_repr():
    item = Item(1, 'test', 'Test item')
    assert repr(item) == "Item(id=1, name=test, description=Test item)"


def test_item_init():
    id = 1
    name = "Test Item"
    description = "This is a test item"
    item = Item(id, name, description)

    assert item.id == id
    assert item.name == name
    assert item.description == description


def test_create_item():
    app = CRUDApp()
    item = app.create_item(1, 'test_item', 'test_description')
    assert item.id == 1
    assert item.name == 'test_item'
    assert item.description == 'test_description'
    assert len(app.items) == 1


def test_read_item():
    app = CRUDApp()
    item1 = app.create_item(1, "Item 1", "Description 1")
    item2 = app.create_item(2, "Item 2", "Description 2")

    assert app.read_item(1) == item1
    assert app.read_item(2) == item2
    assert app.read_item(3) == None  # item with id 3 does not exist


import pytest
from crud import CRUDApp, Item

def test_update_item():
    app = CRUDApp()
    item = app.create_item(1, "test", "test description")
    updated_item = app.update_item(1, "updated", "updated description")
    assert updated_item.name == "updated"
    assert updated_item.description == "updated description"
    assert app.items[0] == updated_item


import pytest
from crud import CRUDApp, Item

@pytest.fixture
def app():
    return CRUDApp()

def test_delete_item(app):
    # create items
    item1 = app.create_item(1, "item1")
    item2 = app.create_item(2, "item2")
    
    # delete an item
    deleted_item = app.delete_item(1)
    
    # check if the item is deleted
    assert deleted_item == item1
    assert len(app.items) == 1
    assert app.read_item(1) == None


def test_list_items():
    # Create an instance of CRUDApp
    app = CRUDApp()

    # Add some items to the app
    app.create_item(1, "Item 1")
    app.create_item(2, "Item 2")
    app.create_item(3, "Item 3")

    # Check that list_items returns the correct list of items
    assert app.list_items() == [
        Item(id=1, name="Item 1", description=None),
        Item(id=2, name="Item 2", description=None),
        Item(id=3, name="Item 3", description=None),
    ]


