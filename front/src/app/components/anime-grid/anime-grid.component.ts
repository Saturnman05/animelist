import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

import { AnimeCardComponent } from '../anime-card/anime-card.component';
import { Anime } from '../../models/anime.model';

@Component({
  selector: 'app-anime-grid',
  imports: [AnimeCardComponent, CommonModule],
  templateUrl: './anime-grid.component.html',
  styleUrl: './anime-grid.component.css',
})
export class AnimeGridComponent {
  @Input() animes: Anime[] = [];
}
