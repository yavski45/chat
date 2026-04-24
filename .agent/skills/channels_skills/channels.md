# Django Channels Skills

Based on the official Django Channels documentation and tutorial, here are the core skills required to build real-time applications:

## 1. Project Setup and Integration
- **Installation**: Installing `channels`, `daphne`, and optionally `channels_redis`.
- **ASGI Configuration**: Setting up `asgi.py` to use `ProtocolTypeRouter` to handle different connection types (HTTP vs WebSocket).
- **Settings configuration**: Updating `INSTALLED_APPS` to include `daphne` (at the top) and the application itself, and setting `ASGI_APPLICATION`.

## 2. Consumers (The Controllers for WebSockets)
- **Synchronous Consumers**: Creating consumers inheriting from `WebsocketConsumer`. Handling `connect()`, `disconnect()`, and `receive()` methods.
- **Asynchronous Consumers**: Creating high-performance consumers inheriting from `AsyncWebsocketConsumer` with `async def` methods and `await`.
- **Scope**: Understanding and utilizing `self.scope` to access connection information (like URL parameters, headers, and the authenticated user).
- **Accepting/Rejecting Connections**: Using `self.accept()` to accept the connection or closing it if unauthorized.

## 3. WebSocket Routing
- **Routing Configuration**: Creating a `routing.py` file using `re_path` or `path` to map WebSocket URLs to consumers using `.as_asgi()`.
- **Middleware**: Wrapping the `URLRouter` with `AuthMiddlewareStack` to populate connection scope with the authenticated user, and `AllowedHostsOriginValidator` for security.

## 4. Channel Layers (Cross-Consumer Communication)
- **Configuration**: Setting up a channel layer backend like `RedisChannelLayer` in `settings.py` via `CHANNEL_LAYERS`.
- **Groups**: 
  - Adding a consumer's channel to a group using `self.channel_layer.group_add(group_name, self.channel_name)`.
  - Removing a channel from a group using `group_discard`.
- **Sending Messages**: Broadcasting messages to all consumers in a group using `self.channel_layer.group_send()`.
- **Handling Group Events**: Creating specific methods on the consumer to handle incoming events from the group based on the event's `type`.
- **Sync/Async Bridging**: Using `asgiref.sync.async_to_sync` to call asynchronous channel layer methods from synchronous consumers.

## 5. Frontend Integration
- **WebSocket API**: Instantiating a `WebSocket` object in JavaScript (`new WebSocket('ws://...')`).
- **Event Listeners**: Handling `onmessage`, `onclose`, and sending data using the `send()` method.
