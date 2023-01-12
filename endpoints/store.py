from endpoints import api_version

store_endpoints = {
    "PET_INVENTORIES_BY_STATUS": api_version.root + "/store/inventory",
    "FIND_DELETE_PURCHASE_ORDER_BY_ID": api_version.root + "/store/order/{orderId}",
    "PLACE_ORDER": api_version.root + "/store/order",
}
