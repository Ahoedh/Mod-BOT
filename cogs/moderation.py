import asyncio
import discord
import time
from discord.ext import commands
from discord import Embed, Color
from typing import Optional
from pathlib import Path

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="ban", aliases=['ban_user', 'delete_user'])
    async def ban_command(self, ctx, user : discord.Member, *, reason):
        await user.ban(reason=reason)

        embed = Embed(color=discord.Color.red())
        embed.set_footer(text=f"Timestamp: {time.ctime()}\nInvoked by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"BAN CASE | BY {ctx.author.mention}",
                        value=f"The user {user.mention} has been banned from the guild.\nREASON: **{reason}**\nMODERATOR: {ctx.author.mention}")

        await ctx.send(embed=embed)

    @commands.command(name="kick", aliases=['kick_user'])
    async def kick_command(self, ctx, user : discord.Member, *, reason):
        await user.ban(reason=reason)

        embed = Embed(color=discord.Color.red())
        embed.set_footer(text=f"Timestamp: {time.ctime()}\nInvoked by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"KICK CASE | BY {ctx.author.mention}",
                        value=f"The user {user.mention} has been kiccked from the guild.\nREASON: **{reason}**\nMODERATOR: {ctx.author.mention}")

        await ctx.send(embed=embed)

    @commands.command(name="warn", aliases=['sudo'])
    async def warn_command(self, ctx, user : discord.Member, *, reason):
        embed = Embed(color=discord.Color.gold())
        embed.set_footer(text=f"Timestamp: {time.ctime()}\nInvoked by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"SUDO COMMAND",
                        value=f"{user.mention} you got a warn in the guild from {ctx.author.mention} for the following reason:\n**{reason}**.\nPlease stop doing wrong!")

        await ctx.send(embed=embed)

    @commands.command(name="mute", aliases=['mute_user'])
    async def mute_command(self, ctx, user : discord.Member, *, reason):
        role = get(ctx.guild.roles, name="puttherolenamehere")
        await user.add_roles(role)

        embed = Embed(color=discord.Color.gold())
        embed.set_footer(text=f"Timestamp: {time.ctime()}\nInvoked by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"MUTE CASE | {ctx.author.mention}",
                        value=f"The user {user.mention} has been muted in the server for the following reason:\n**{reason}**.\nMODERATOR: {ctx.author.mention}")

        await ctx.send(embed=embed)

    @commands.command(name="unmute", aliases=['unmute_user'])
    async def unmute_command(self, ctx, user : discord.Member):
        role = get(ctx.guild.roles, name="puttherolenamehere")
        await user.remove_roles(role)

        embed = Embed(color=discord.Color.gold())
        embed.set_footer(text=f"Timestamp: {time.ctime()}\nInvoked by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"UNMUTE COMMAND",
                        value=f"{user.mention} has been unmuted in the server.\nMODERATOR: {ctx.author.mention}")

        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        bad_words = ["dog", "cat"]

        if get(ctx.guild.roles, name="puttherolenamehere")
            for word in bad_words:
                if message.content.count(str(word)) > 0:
                    embed = Embed(color=discord.Color.gold())
                    embed.set_footer(text=f"Timestamp: {time.ctime()}\nInvoked by {ctx.author}", icon_url=ctx.author.avatar_url)
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    embed.add_field(name=f"AUTOMODERATION SYSTEM",
                                    value=f"{message.author.mention} said a bad word. You can't say that word.")

                    await ctx.send(embed=embed)
                    await message.author.add_roles(role)

        else:
            staff_role = get(ctx.guild.roles, name="puttherolenamehere")
            for word in bad_words:
                if message.content.count(str(word)) > 0:
                    embed = Embed(color=discord.Color.gold())
                    embed.set_footer(text=f"Timestamp: {time.ctime()}\nInvoked by {ctx.author}", icon_url=ctx.author.avatar_url)
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    embed.add_field(name=f"AUTOMODERATION SYSTEM",
                                    value=f"{message.author.mention} said a bad word. You can't say that word.")

                    await ctx.send(embed=embed)
                    await ctx.send(f"{staff.mention} check the message below.")

        @ban_command.error
        async def ban_command_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                embed = Embed(color=discord.Color.gold())
                embed.set_footer(text=f"Timestamp: {time.ctime()})
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.add_field(name=f"BAN COMMAND ERROR",
                                value=f"{message.author.mention} you're messing a required argument in the command. Please retry.")

                await ctx.send(embed=embed)

        @kick_command.error
        async def kick_command_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                embed = Embed(color=discord.Color.gold())
                embed.set_footer(text=f"Timestamp: {time.ctime()})
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.add_field(name=f"BAN COMMAND ERROR",
                                value=f"{message.author.mention} you're messing a required argument in the command. Please retry.")

                await ctx.send(embed=embed)

        @warn_command.error
        async def warn_command_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                embed = Embed(color=discord.Color.gold())
                embed.set_footer(text=f"Timestamp: {time.ctime()})
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.add_field(name=f"BAN COMMAND ERROR",
                                value=f"{message.author.mention} you're messing a required argument in the command. Please retry.")

                await ctx.send(embed=embed)

        @mute_command.error
        async def mute_command_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                embed = Embed(color=discord.Color.gold())
                embed.set_footer(text=f"Timestamp: {time.ctime()})
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.add_field(name=f"BAN COMMAND ERROR",
                                value=f"{message.author.mention} you're messing a required argument in the command. Please retry.")

                await ctx.send(embed=embed)

        @unmute_command.error
        async def unmute_command_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                embed = Embed(color=discord.Color.gold())
                embed.set_footer(text=f"Timestamp: {time.ctime()})
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.add_field(name=f"BAN COMMAND ERROR",
                                value=f"{message.author.mention} you're messing a required argument in the command. Please retry.")

                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moderation(client))
