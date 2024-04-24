// authentication.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  login(username: string, password: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/login/`, { username, password }).pipe(
      tap(response => {
        // Store JWT token in local storage
        localStorage.setItem('token', response.access);
      })
    );
  }

  logout(): void {
    // Remove JWT token from local storage
    localStorage.removeItem('token');
  }
}
