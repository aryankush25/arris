import requests

from arris.schemas.shopify_theme import (
  create_store_theme,
  update_store_theme,
  get_store_theme_by_id,
  delete_store_theme,
  get_store_themes,
)

from arris.schemas.shopify_store import get_store_by_name

def createStoreTheme(name: str, role: str, src: str, storeName: str):
  try:
    print("Creating Theme")
    store = get_store_by_name(name=storeName)

    if not store:
      return "Store not found"

    response = requests.post(f"https://{storeName}.myshopify.com/admin/api/2024-01/themes.json",
      data={
        "theme": {
          "name": name,
          "role": role,
          "src": src
        }  
      }, 
      headers={
        'X-Shopify-Access-Token': store.access_token,
        'Content-Type': 'application/json'
      }
    )

    theme = response.json().get("theme")
    create_store_theme(
      theme_id=theme.get("id"),
      name=theme.get("name"),
      role=theme.get("role"),
      email=store.email,
      store_id=store.id,
      admin_graphql_api_id=theme.get("admin_graphql_api_id"),
      theme_store_id=theme.get("theme_store_id"),
      previewable=theme.get("previewable"),
      processing=theme.get("processing")
    )

    return theme
  except Exception as error:
      print("Craete Theme Error", error)

def updateStoreTheme(storeName: str, role: str, name: str, id: str):
  try:
    print("Updating Theme")
    store = get_store_by_name(name=storeName)

    if not store:
      return "Store not found"
    
    theme = get_store_theme_by_id(id=id)
    
    payload = {
      "theme": {
        "id": theme.theme_id
      }
    }

    if role:
      payload["theme"]["role"] = role
    
    if name:
      payload["theme"]["name"] = name

    response = requests.put(f"https://{storeName}.myshopify.com/admin/api/2024-01/themes.json",
      data=payload,
      headers={
        'X-Shopify-Access-Token': store.access_token,
        'Content-Type': 'application/json'
      }
    )

    updatedTheme = response.json().get("theme")

    update_store_theme(id=theme.id, role=updatedTheme.get("role"))
    return get_store_theme_by_id(id=id)
  except Exception as error:
      print("Update Theme Error", error)
      
def getStoreThemes(storeName: str):
  try:
    print("Getting Themes")
    store = get_store_by_name(name=storeName)

    if not store:
      return "Store not found"

    return get_store_themes(storeId=store.id)
  except Exception as error:
      print("Get Themes Error", error)

def getStoreThemeById(themeId: str, storeName: str):
  try:
    print("Getting Theme by ID")
    store = get_store_by_name(name=storeName)

    if not store:
      return "Store not found"
    
    return get_store_theme_by_id(id=themeId)
  except Exception as error:
      print("Get Theme by ID Error", error)

def deleteStoreTheme(id: str, storeName: str):
  try:
    print("Deleting Theme")
    store = get_store_by_name(name=storeName)

    if not store:
      return "Store not found"
    
    theme = get_store_theme_by_id(id=id)
    
    if not theme:
      return "Theme not found"

    requests.delete(f"https://{storeName}.myshopify.com/admin/api/2024-01/themes/{theme.theme_id}.json",
      headers={
        'X-Shopify-Access-Token': store.access_token,
        'Content-Type': 'application/json'
      }
    )
    
    return delete_store_theme(id=theme.id)
  except Exception as error:
      print("Delete Theme Error", error)
