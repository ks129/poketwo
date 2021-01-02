alter table "public"."caught_pokemon" add column "form_id" integer not null;

alter table "public"."caught_pokemon" add constraint "caught_pokemon_form_id_fkey" FOREIGN KEY (form_id) REFERENCES pokemon_forms(id) ON DELETE CASCADE;

