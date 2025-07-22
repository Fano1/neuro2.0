from characterai import aiocai, sendCode, authUser
import asyncio

async def main():
    try:
        email = input('YOUR EMAIL: ')

    
        print('Sending verification link to your email...')
        sendCode(email)
        print('Verification link has been sent, please check your email')


        print('\nPlease copy the ENTIRE verification link from your email')
        verification_link = input('Enter the verification link: ')

        print('Getting token...')
        token = authUser(verification_link, email)

        print('\nYour token has been successfully generated:')
        print(f'TOKEN: {token}')
        


    except Exception as e:
        print(f'\nError occurred: {str(e)}')

if __name__ == "__main__":
    asyncio.run(main())