from django.urls import path


urlpatterns = [
    path(
        'api/auth/refister',
        TokenCreateView.as_view(), name='token_create',
    )
    # path(
    #     'api/auth/refresh',
    #     TokenRefreshView.as_view(), name='token_refresh',
    # )
]