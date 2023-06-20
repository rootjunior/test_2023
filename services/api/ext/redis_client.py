from redis.asyncio import Redis


class RedisClient(Redis):
    async def write_data(self, phone: str, address: str) -> None:
        await self.set(phone, address)
        self.close()

    async def check_data(self, phone: str) -> dict:
        if await self.exists(phone):
            address = await self.get(phone)
            self.close()
            return {"phone": phone, "address": address}
