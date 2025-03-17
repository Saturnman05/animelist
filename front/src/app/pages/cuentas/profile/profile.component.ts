import { Component, inject, OnInit } from '@angular/core';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { Router } from '@angular/router';

import { NavBarComponent } from '../../../components/nav-bar/nav-bar.component';
import { AuthService } from '../../../services/auth/auth.service';

@Component({
  selector: 'app-profile',
  imports: [
    MatButtonModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    NavBarComponent,
    ReactiveFormsModule,
  ],
  templateUrl: './profile.component.html',
  styleUrl: '../login/login.component.scss',
})
export class ProfileComponent implements OnInit {
  profileForm!: FormGroup;
  private fieldsDisabled: boolean = true;

  private AuthService = inject(AuthService);
  private fb = inject(FormBuilder);
  private router = inject(Router);

  ngOnInit(): void {
    if (!this.AuthService.isAuthenticated$) {
      this.router.navigate(['/login']);
      return;
    }

    this.initForm();
  }

  private initForm(): void {
    this.profileForm = this.fb.group({
      username: [
        { value: 'Username', disabled: this.fieldsDisabled },
        Validators.required,
      ],
      email: [
        { value: 'Email@email.com', disabled: this.fieldsDisabled },
        Validators.required,
      ],
    });
  }

  onChangeDisabled(): void {
    this.fieldsDisabled = !this.fieldsDisabled;

    if (this.fieldsDisabled) {
      this.profileForm.controls['username'].disable();
      this.profileForm.controls['email'].disable();
      return;
    }

    this.profileForm.controls['username'].enable();
    this.profileForm.controls['email'].enable();
  }

  onSubmit(): void {
    return;
  }
}
