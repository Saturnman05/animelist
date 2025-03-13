import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class TokenService {
  private readonly TOKEN_KEY = 'authToken';
  private readonly USER_KEY = 'authUser';

  saveToken(token: string): void {
    if (typeof window !== 'undefined')
      localStorage.setItem(this.TOKEN_KEY, token);
  }

  getToken(): string | null {
    if (typeof window !== 'undefined')
      return localStorage.getItem(this.TOKEN_KEY);
    return null;
  }

  removeToken(): void {
    if (typeof window !== 'undefined') localStorage.removeItem(this.TOKEN_KEY);
  }

  saveUser(user: any): void {
    if (typeof window !== 'undefined')
      localStorage.setItem(this.USER_KEY, JSON.stringify(user));
  }

  getUser(): any {
    if (!(typeof window !== 'undefined')) {
      const user = localStorage.getItem(this.USER_KEY);
      return user ? JSON.parse(user) : null;
    }
  }

  removeUser(): void {
    if (typeof window !== 'undefined') localStorage.removeItem(this.USER_KEY);
  }

  clear(): void {
    if (typeof window !== 'undefined') localStorage.clear();
  }

  isLoggedIn(): boolean {
    return !!this.getToken();
  }
}
