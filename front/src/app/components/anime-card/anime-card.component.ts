import { Component, Input } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { Anime } from '../../models/anime.model';

@Component({
  selector: 'app-anime-card',
  imports: [MatCardModule],
  templateUrl: './anime-card.component.html',
  styleUrl: './anime-card.component.css',
})
export class AnimeCardComponent {
  @Input() anime!: Anime;

  public get title(): string {
    return this.anime?.title ?? '';
  }

  public get author(): string {
    return this.anime?.author ?? '';
  }

  public get genre(): string {
    return this.anime?.genre ?? '';
  }

  public get amountEpisodes(): number {
    return this.anime?.amountEpisodes ?? 0;
  }
}
