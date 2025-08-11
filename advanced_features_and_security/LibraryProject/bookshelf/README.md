# Django Permissions & Groups Setup

## Permissions
- `can_edit` → Allows editing of articles.
- `can_create` → Allows creating of articles.

## Groups
- **Editors**: `can_edit`, `can_create`.
- **Viewers**: No custom permissions (read-only).
- **Admins**: All permissions.

## Usage in Views
```python
@permission_required('yourapp.can_create', raise_exception=True)
def create_article(request): ...

@permission_required('yourapp.can_edit', raise_exception=True)
def edit_article(request, article_id): ...
