import { Component, inject, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { NavBarComponent } from '../../../components/nav-bar/nav-bar.component';
import { AuthService } from '../../../services/auth/auth.service';

@Component({
  selector: 'app-profile',
  imports: [NavBarComponent],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css',
})
export class ProfileComponent implements OnInit {
  private AuthService = inject(AuthService);
  private router = inject(Router);

  ngOnInit(): void {
    if (!this.AuthService.isAuthenticated$) {
      this.router.navigate(['/login']);
    }
  }
}
