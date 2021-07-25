import discord 
from discord.ext import commands
import wikipedia

class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    @commands.command(name='Wiki',
                      aliases=['wikipedia', 'buscar', 'search'],
                      help='Pesquisa no Wikipedia.')
    async def wiki(self, ctx, *, args):
        wikipedia.set_lang('pt')
        wiki_logo = """
        https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Wikipedia_svg_logo.svg/1200px-Wikipedia_svg_logo.svg.png
        """

        def get_summary(page):
            p = page.summary.split('.')
            return f'{p[0]}. {p[1]}. {p[2]}. {p[3]}. {p[4]}.'

        result = wikipedia.search(args, results=10)
        embed = discord.Embed(color=rbColor())
        embed.set_thumbnail(url=wiki_logo)
        embed.add_field(name='Estes são os resultados:',
                        value=f'1. **{result[0]}**\n2. **{result[1]}**\n'
                              f'3. **{result[2]}**\n4. **{result[3]}**\n'
                              f'5. **{result[4]}**\n6. **{result[5]}**\n'
                              f'7. **{result[6]}**\n8. **{result[7]}**\n'
                              f'9. **{result[8]}**\n10. **{result[9]}**',
                        inline=False)
        embed.set_footer(text='Escreve o número correspondente'
                              'ao artigo que deseja obter.')
        await ctx.send(embed=embed)

        def is_author(m):
            return m.author == ctx.author

        try:
            selected_page = await self.bot.wait_for('message', check=is_author,
                                                    timeout=45.0)
        except asyncio.TimeoutError:
            await ctx.send('Seu pedido expirou :(.')

        else:
            index = int(selected_page.content) - 1
            page = wiki.page(result[index])
            e = discord.Embed(color=rbColor(), title=page.title,
                              description=get_summary(page))
            e.set_author(name=f'{page.title} em Wikipedia',
                         url=page.canonicalurl)
            e.set_thumbnail(url=wiki_logo)
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Wiki(bot))