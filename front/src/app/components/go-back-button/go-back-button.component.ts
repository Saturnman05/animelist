import { Component, Input } from '@angular/core';
import { MatButton } from '@angular/material/button';
import { MatIcon } from '@angular/material/icon';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-go-back-button',
  imports: [MatButton, MatIcon, RouterModule],
  templateUrl: './go-back-button.component.html',
  styleUrl: './go-back-button.component.css',
})
export class GoBackButtonComponent {
  @Input() route!: string;
}
